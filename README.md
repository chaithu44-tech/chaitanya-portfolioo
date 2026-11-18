# Chelamsetty Chaitanya — Editorial Portfolio Website

An editorial, magazine-grade portfolio website designed faithfully using the provided reference layout, created exclusively with Chelamsetty Chaitanya's resume credentials and portrait photo.

---

## 🎨 Design System & Reference Mapping

| Reference Section | Reference Element | Chaitanya's Implementation |
|---|---|---|
| **Top Bar** | `✻ WEB DESIGNER` & `AVAILABLE FOR FREELANCE ⟶` | `✻ AI & SOFTWARE DEVELOPER` & `AVAILABLE FOR OPPORTUNITIES ⟶` |
| **Edge Margins** | Rotated vertical typographic labels | `MACHINE LEARNING / FULL-STACK AI / PYTHON ARCHITECTURE` |
| **Headline** | Condensed display `PORTFOLIO` | Giant condensed uppercase `PORTFOLIO` (Bebas Neue) |
| **Hero Left** | `HELLO, I'M ALEX MORGAN`, subtitle, bio, script signature | `HELLO, I'M CHELAMSETTY CHAITANYA`, `AI & MACHINE LEARNING ENGINEER`, AIML career objective bio, cursive script signature |
| **Hero Right** | Terracotta circular backdrop + photo cutout + rotating stamp | Terracotta circle `#C36746` + Chaitanya's transparent cutout portrait + revolving SVG badge (`AVAILABLE FOR OPPORTUNITIES • BENGALURU, INDIA`) |
| **Selected Projects** | 4-card editorial preview (`01`, `02`, `03`, `04`) | 4 core modules from Chaitanya's AI Career Platform: `01 Career Engine`, `02 Resume Parser`, `03 FastAPI Core`, `04 Adaptive Roadmaps` |
| **Skills & Expertise** | 3-column layout: progress bars, central quote, 4 circular icon cards | 1) Technical skill bars (Python & FastAPI, Java, C, Gemini API, SQLite, Docker)<br>2) Central editorial quote<br>3) 4 feature cards with terracotta circular icons |
| **Achievements** | 3 testimonial cards with quotation marks, badges, and roles | 3 milestone cards: Smart India Hackathon (National Stage), Jain University (9.00 & 8.625 SGPA), 12th (92.5%) & 10th (83%) Board scores |
| **Footer / Contact** | `LET'S CREATE SOMETHING GREAT`, QR Code, 3 contact rows | `LET'S CREATE SOMETHING GREAT`, scannable QR Code with hand-drawn curly pointer arrow, Email (`chaithuniva44@gmail.com`), Phone (`+91 6302183467`), Location, and University |

---

## 🚀 How to Run with Python

### Option 1: Run the Dedicated Python Server
```bash
cd /Users/bunnyroyal/.gemini/antigravity/scratch/chaitanya-portfolio
python3 app.py
```
Or specify a custom port:
```bash
python3 app.py 8080
```
Then open **[http://localhost:8000](http://localhost:8000)** (or the displayed port) in any web browser.

### Option 2: Open Directly in Browser
You can also open `index.html` directly:
```bash
open /Users/bunnyroyal/.gemini/antigravity/scratch/chaitanya-portfolio/index.html
```

---

## 📁 Project Structure

```
chaitanya-portfolio/
├── app.py                      # Dedicated multi-threaded Python web server + API
├── index.html                  # Main editorial portfolio HTML
├── README.md                   # Project documentation & run guide
└── static/
    ├── css/
    │   └── styles.css          # Editorial typography, color variables, grid layouts & animations
    ├── js/
    │   └── main.js             # Scroll animations, click-to-copy, and stamp badge interaction
    └── images/
        ├── chaitanya.png       # Transparent cutout portrait of Chelamsetty Chaitanya
        ├── project_1.jpg       # Career Engine preview card
        ├── project_2.jpg       # Resume Parser preview card
        ├── project_3.jpg       # FastAPI Core preview card
        ├── project_4.jpg       # Adaptive Roadmaps preview card
        ├── qr_code.png         # Scannable QR code
        ├── badge_sih.png       # Smart India Hackathon badge
        ├── badge_jain.png      # Jain University emblem badge
        └── badge_acad.png      # Academic distinction badge
```
