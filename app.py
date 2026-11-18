#!/usr/bin/env python3
"""
Chelamsetty Chaitanya - Editorial Portfolio Web Server
Runs a dedicated Python web server to serve the portfolio website.
"""

import http.server
import json
import os
import socket
import socketserver
import sys
import urllib.parse
from http import HTTPStatus

DEFAULT_PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Profile data matching the portfolio and resume
PROFILE_DATA = {
    "name": "Chelamsetty Chaitanya",
    "degree": "B.Tech in Artificial Intelligence & Machine Learning",
    "institution": "Jain Deemed-to-be University, Bengaluru",
    "status": "Currently pursuing 2nd Year, 3rd Semester",
    "contact": {
        "email": "chaithuniva44@gmail.com",
        "phone": "+91 6302183467",
        "location": "Bengaluru, Karnataka (Remote Worldwide)"
    },
    "technical_skills": [
        "Python", "FastAPI", "Java", "C", "Google Gemini API",
        "SQLite", "SQLAlchemy", "PyMuPDF", "Docker", "HTML", "CSS", "Tailwind CSS", "JavaScript"
    ],
    "projects": [
        {
            "id": 1,
            "title": "Career Compatibility Engine",
            "category": "AI Compatibility & Matching",
            "description": "Built a weighted scoring system to identify skill gaps and match student profiles with industry roles."
        },
        {
            "id": 2,
            "title": "Intelligent Resume Parser",
            "category": "Gemini AI & Document NLP",
            "description": "Implemented PDF/DOCX resume parsing and AI-based analysis to extract skills, certifications, and recommendations."
        },
        {
            "id": 3,
            "title": "FastAPI Backend Core",
            "category": "Backend APIs & Security",
            "description": "Developed backend APIs using Python and FastAPI with SQLite, SQLAlchemy, JWT auth, and 15 automated test suites."
        },
        {
            "id": 4,
            "title": "Adaptive Learning Roadmaps",
            "category": "Full-Stack Career Platform",
            "description": "Personalized roadmaps with progress tracking, dedicated student, recruiter, and administrator portals."
        }
    ],
    "academics": {
        "tenth": "83%",
        "twelfth": "92.5%",
        "sem_1_sgpa": "8.625",
        "sem_2_sgpa": "9.00"
    },
    "achievements": [
        "Smart India Hackathon — Qualified Participant (National Stage)",
        "Academic Excellence: Maintained 8.625 SGPA (Sem 1) and 9.00 SGPA (Sem 2)"
    ],
    "personal_strengths": [
        "Problem-solving", "Quick learning", "Teamwork and collaboration",
        "Adaptability", "Interest in emerging technologies"
    ]
}

class PortfolioHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Serve JSON API endpoint
        if self.path in ("/api/profile", "/api/profile/"):
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(PROFILE_DATA, indent=2).encode("utf-8"))
            return
        
        # Default route to index.html
        if self.path in ("/", ""):
            self.path = "/index.html"
            
        return super().do_GET()

    def do_POST(self):
        # Handle contact form submissions
        if self.path == "/api/contact":
            content_length = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_length)
            try:
                data = json.loads(post_body.decode("utf-8"))
            except Exception:
                data = urllib.parse.parse_qs(post_body.decode("utf-8"))

            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            response = {
                "status": "success",
                "message": "Thank you for reaching out! Chelamsetty Chaitanya will connect with you soon.",
                "data_received": data
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        self.send_error(HTTPStatus.NOT_FOUND, "Endpoint not found")

    def end_headers(self):
        # Enable caching controls and proper MIME types
        if self.path.endswith(".css"):
            self.send_header("Content-Type", "text/css; charset=utf-8")
        elif self.path.endswith(".js"):
            self.send_header("Content-Type", "application/javascript; charset=utf-8")
        elif self.path.endswith(".png"):
            self.send_header("Content-Type", "image/png")
        elif self.path.endswith(".jpg") or self.path.endswith(".jpeg"):
            self.send_header("Content-Type", "image/jpeg")
        elif self.path.endswith(".svg"):
            self.send_header("Content-Type", "image/svg+xml")
        super().end_headers()

def find_available_port(preferred=DEFAULT_PORT):
    ports_to_try = [preferred, 8000, 8088, 8081, 8090, 8501, 3000]
    for p in ports_to_try:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("127.0.0.1", p))
                return p
        except OSError:
            continue
    # Fallback to random dynamic port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]

class ReusableThreadingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

def run_server(port=None):
    if port is None:
        if len(sys.argv) > 1 and sys.argv[1].isdigit():
            port = int(sys.argv[1])
        else:
            port = find_available_port(DEFAULT_PORT)

    server_address = ("127.0.0.1", port)
    httpd = ReusableThreadingServer(server_address, PortfolioHTTPRequestHandler)
    
    url = f"http://localhost:{port}"
    print("=" * 70)
    print("✨ CHELAMSETTY CHAITANYA — EDITORIAL PORTFOLIO SERVER")
    print(f"🌐 Website URL:  {url}")
    print(f"📁 Root Dir:     {DIRECTORY}")
    print(f"📡 API Endpoint: {url}/api/profile")
    print("=" * 70)
    print("Serving portfolio with Python. Press Ctrl+C to terminate.")

    # Optional auto-open
    if "--open" in sys.argv:
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception:
            pass

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping portfolio server...")
        httpd.server_close()
        sys.exit(0)

if __name__ == "__main__":
    run_server()
