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

## 🔑 How to Access the Files — Step-by-Step Guide

Choose the method that suits you best.

---

### Method 1 — Browse files on GitHub (no download required)

1. Open your browser and go to:
   ```
   https://github.com/YOC21/fluent-english-app
   ```
2. You will see a list of all files in the repository root.
3. Click on any filename to view its contents in your browser.
   - Example: click **`index.html`** to see the full source code of the English-learning app.
   - Example: click **`past-events-tracker.html`** to see the medical events tracker source code.
4. To view a file in **raw** form, open the file and click the **Raw** button (top-right of the file view).

---

### Method 2 — Download all files as a ZIP (no Git required)

1. Go to `https://github.com/YOC21/fluent-english-app`.
2. Click the green **`<> Code`** button near the top-right.
3. Select **Download ZIP**.
4. A file named `fluent-english-app-main.zip` (or similar) will be saved to your **Downloads** folder.
5. Locate the ZIP in your Downloads folder and **extract / unzip** it:
   - **Windows**: right-click the ZIP → *Extract All…*
   - **macOS**: double-click the ZIP
   - **Linux**: `unzip fluent-english-app-main.zip`
6. Open the extracted `fluent-english-app-main/` folder — all files are inside.

---

### Method 3 — Clone the repository with Git

> Requires [Git](https://git-scm.com/downloads) to be installed.

1. Open a terminal (Command Prompt, PowerShell, or any shell).
2. Navigate to the folder where you want to save the project:
   ```bash
   cd ~/Documents        # or any folder you prefer
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/YOC21/fluent-english-app.git
   ```
4. Enter the newly created folder:
   ```bash
   cd fluent-english-app
   ```
5. List the files to confirm everything is there:
   ```bash
   ls          # macOS / Linux
   dir         # Windows
   ```
   You should see: `index.html`, `past-events-tracker.html`, `past_events_tracker.py.py`, `manifest.json`, `service-worker.js`, `generate_icons.py`, `icons/`, `README.md`, `QUICK_START.md`.

---

### Method 4 — Open the HTML apps in your browser (offline)

> Works after downloading via Method 2 or cloning via Method 3.

**FluentEnglish Pro PWA (`index.html`)**

1. Open your file manager and navigate to the `fluent-english-app` folder.
2. Double-click **`index.html`**.  
   It will open in your default browser and the full app will load — no internet connection needed.

**Phoenix Medical Past Events Tracker (`past-events-tracker.html`)**

1. In the same folder, double-click **`past-events-tracker.html`**.  
   It will open in your default browser showing the filterable table of medical conferences.

---

### Method 5 — Run the Python script (`past_events_tracker.py.py`)

> Requires Python 3. Install from [python.org](https://www.python.org/downloads/).

1. Open a terminal and navigate to the project folder:
   ```bash
   cd fluent-english-app
   ```
2. Install required Python packages (one-time setup):
   ```bash
   pip install pandas requests beautifulsoup4 ddgs openpyxl
   ```
3. Run the script:
   ```bash
   python past_events_tracker.py.py
   ```
4. A timestamped `.xlsx` file (e.g. `past_events_20251015_143022.xlsx`) will be created **in the same folder** where you ran the command. Open it with Excel, LibreOffice Calc, or Google Sheets.

---

### Method 6 — Access the live hosted URLs (GitHub Pages)

If GitHub Pages is enabled for this repository, the HTML files are accessible directly in any browser without downloading anything:

| File | Live URL |
|------|----------|
| `index.html` | `https://yoc21.github.io/fluent-english-app/` |
| `past-events-tracker.html` | `https://yoc21.github.io/fluent-english-app/past-events-tracker.html` |

> **To enable GitHub Pages** (repository owner only):
> 1. Go to the repository on GitHub.
> 2. Click **Settings** → **Pages** (left sidebar).
> 3. Under *Source*, select the **main** branch and click **Save**.
> 4. Wait ~1 minute, then visit the URLs above.

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
