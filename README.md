# fluent-english-app

A Progressive Web App (PWA) for mastering English fluency, plus a Phoenix Medical past-events tracker tool.

---

## 📁 Where the Files Are Saved

All files live in the **root of this repository**:

```
fluent-english-app/                         ← repository root
│
├── index.html                              # FluentEnglish Pro PWA — main application (full SPA)
├── manifest.json                           # PWA manifest (name, icons, theme colour, shortcuts)
├── service-worker.js                       # Service worker — offline caching
│
├── past-events-tracker.html               # Phoenix Medical Past Events Tracker (static web app)
│                                           #   • Displays 6 verified medical conferences (2025-26)
│                                           #   • Category / review filters, full-text search
│                                           #   • CSV export
│                                           #   • Mirrors the logic in past_events_tracker.py.py
│
├── past_events_tracker.py.py              # Python backend script (source of truth for events data)
│                                           #   Note: the double .py.py extension is how the file was uploaded.
│                                           #   • Searches DuckDuckGo for past medical events
│                                           #   • Exports results to .xlsx via pandas / openpyxl
│
├── generate_icons.py                       # Utility: generates all 8 PWA icon sizes in icons/
│
├── icons/                                  # PWA icons (8 sizes, PNG)
│   ├── icon-72x72.png
│   ├── icon-96x96.png
│   ├── icon-128x128.png
│   ├── icon-144x144.png
│   ├── icon-152x152.png
│   ├── icon-192x192.png
│   ├── icon-384x384.png
│   └── icon-512x512.png
│
├── README.md                               # This file
├── QUICK_START.md                          # Short install & usage guide
├── .gitignore
└── .gitattributes
```

---

## 🌐 FluentEnglish Pro PWA (`index.html`)

A self-contained single-page application. Open `index.html` in any browser, or host it to install as an Android/iOS PWA.

**Features:** Shadowing practice · Intensive listening timer · Idioms flashcards · Vocabulary journal · 21-day challenge · Progress tracker.

## 🏥 Phoenix Medical Past Events Tracker (`past-events-tracker.html`)

Open `past-events-tracker.html` in any browser — no server required.

**Features:** Filter by category (Neonatology, Maternal/OB-GYN, Paediatrics, Perinatology) · Filter by review rating · Full-text search · CSV export · Search-query reference panel.

## 🐍 Python Events Script (`past_events_tracker.py.py`)

Requires Python 3 with `pandas`, `requests`, `beautifulsoup4`, and `ddgs`.

```bash
python past_events_tracker.py.py
```

Outputs a timestamped `.xlsx` file in the current directory with all discovered past medical events.

---

## 🚀 Hosting on GitHub Pages

1. Go to **Settings → Pages** in this repository.
2. Select the branch (`main`) as the source.
3. Your app will be live at `https://<your-username>.github.io/fluent-english-app/`.

Both `index.html` and `past-events-tracker.html` will be accessible at their respective paths.
