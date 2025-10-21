# 🧠 File Detector & Malware Scanner

A simple cybersecurity project that:

- Identifies file types using magic bytes (headers)
- Generates file hashes (MD5, SHA1, SHA256)
- Scans for known malware signatures (optional later)
- Uses a command-line interface (CLI)

---

## ⚙️ How to Run

```bash
# 1️⃣ Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the scanner
python3 -m app.cli sample_data/eicar.txt

