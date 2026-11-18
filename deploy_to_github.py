#!/usr/bin/env python3
"""
Deploy Chelamsetty Chaitanya's Portfolio directly to GitHub
Uses the GitHub REST API (Pure Python, zero external dependencies).
"""

import base64
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO_NAME = "chaitanya-portfolio"
REPO_DESC = "Editorial portfolio website of Chelamsetty Chaitanya — AI & Machine Learning Engineer"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configure SSL Context (handles macOS Python missing certs bundle)
def get_ssl_context():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        pass
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx
    except Exception:
        return ssl._create_unverified_context()

SSL_CONTEXT = get_ssl_context()

def make_github_request(url, method="GET", data=None, token=None):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Chaitanya-Portfolio-Deployer/1.0",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    encoded_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req, context=SSL_CONTEXT) as response:
            res_body = response.read().decode("utf-8")
            return json.loads(res_body) if res_body else {}
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        try:
            return {"error": True, "status": e.code, "details": json.loads(err_msg)}
        except Exception:
            return {"error": True, "status": e.code, "details": err_msg}

def deploy():
    print("=" * 70)
    print("🚀 GITHUB DIRECT DEPLOYER — CHELAMSETTY CHAITANYA PORTFOLIO")
    print("=" * 70)

    # 1. Get Token
    token = os.environ.get("GITHUB_TOKEN")
    if not token and len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        token = sys.argv[1]

    if not token:
        print("\n🔑 Please enter your GitHub Personal Access Token:")
        try:
            token = input("GitHub Token: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nDeployment cancelled.")
            sys.exit(1)

    if not token:
        print("❌ Error: GitHub Token cannot be empty.")
        sys.exit(1)

    # 2. Verify user
    print("\n[1/5] Verifying GitHub user credentials...")
    user_info = make_github_request("https://api.github.com/user", token=token)
    if "error" in user_info:
        print(f"❌ Authentication failed: {user_info.get('details')}")
        print("Tip: Ensure your token has 'repo' permissions.")
        sys.exit(1)

    username = user_info.get("login")
    print(f"✅ Authenticated as: {username} ({user_info.get('name', 'Developer')})")

    # 3. Create or check repository
    print(f"\n[2/5] Checking repository '{REPO_NAME}' on GitHub...")
    repo_info = make_github_request(f"https://api.github.com/repos/{username}/{REPO_NAME}", token=token)

    if "error" in repo_info and repo_info.get("status") == 404:
        print(f"Creating new public repository '{REPO_NAME}'...")
        create_payload = {
            "name": REPO_NAME,
            "description": REPO_DESC,
            "private": False,
            "auto_init": True
        }
        repo_info = make_github_request("https://api.github.com/user/repos", method="POST", data=create_payload, token=token)
        if "error" in repo_info:
            print(f"❌ Failed to create repository: {repo_info.get('details')}")
            sys.exit(1)
        print("✅ Repository created successfully!")
    else:
        print(f"✅ Repository '{REPO_NAME}' found on your GitHub account.")

    # 4. Gather all files to upload
    print("\n[3/5] Preparing files for upload...")
    files_to_upload = []
    for root, dirs, files in os.walk(BASE_DIR):
        if "__pycache__" in root or ".git" in root:
            continue
        for f in files:
            if f.endswith(".pyc") or f in ("screenshot_portfolio.png",):
                continue
            abs_path = os.path.join(root, f)
            rel_path = os.path.relpath(abs_path, BASE_DIR).replace("\\", "/")
            files_to_upload.append((rel_path, abs_path))

    print(f"Found {len(files_to_upload)} files to upload to GitHub:")
    for rel_path, _ in files_to_upload:
        print(f"  • {rel_path}")

    # 5. Upload files via GitHub REST API
    print("\n[4/5] Uploading files to GitHub...")
    for rel_path, abs_path in files_to_upload:
        with open(abs_path, "rb") as fp:
            content_b64 = base64.b64encode(fp.read()).decode("utf-8")

        # Check if file exists to get its SHA (required for updating)
        file_check = make_github_request(f"https://api.github.com/repos/{username}/{REPO_NAME}/contents/{rel_path}", token=token)
        sha = None
        if not file_check.get("error") and "sha" in file_check:
            sha = file_check["sha"]

        payload = {
            "message": f"Upload {rel_path} for portfolio website",
            "content": content_b64
        }
        if sha:
            payload["sha"] = sha

        put_res = make_github_request(
            f"https://api.github.com/repos/{username}/{REPO_NAME}/contents/{rel_path}",
            method="PUT",
            data=payload,
            token=token
        )

        if "error" in put_res:
            print(f"  ❌ Failed to upload {rel_path}: {put_res.get('details')}")
        else:
            print(f"  ✅ Uploaded: {rel_path}")

    # 6. Enable GitHub Pages
    print("\n[5/5] Activating GitHub Pages for live hosting...")
    pages_payload = {
        "source": {
            "branch": "main",
            "path": "/"
        }
    }
    pages_res = make_github_request(f"https://api.github.com/repos/{username}/{REPO_NAME}/pages", method="POST", data=pages_payload, token=token)
    
    live_url = f"https://{username}.github.io/{REPO_NAME}/"
    repo_url = f"https://github.com/{username}/{REPO_NAME}"

    print("\n" + "=" * 70)
    print("🎉 DEPLOYMENT COMPLETE!")
    print(f"📦 GitHub Repository: {repo_url}")
    print(f"🌍 Live Website URL:  {live_url}")
    print("=" * 70)
    print("Note: GitHub Pages may take 1-2 minutes to finish building the first time.\n")

if __name__ == "__main__":
    deploy()
