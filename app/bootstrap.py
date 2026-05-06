"""
Allegro AI - Bootstrap launcher
Handles venv creation, pip install, then starts the server.
Called by windows/start.bat — all logic here so .bat stays minimal.
"""
import os
import sys
import subprocess
from pathlib import Path

APP_DIR = Path(__file__).parent.resolve()
VENV_DIR = APP_DIR / "venv"
VENV_PY  = VENV_DIR / "Scripts" / "python.exe"   # Windows
VENV_PIP = VENV_DIR / "Scripts" / "pip.exe"

SEP = "=" * 50

def step(n, msg):
    print(f"\n[{n}/4] {msg}...")

def ok(msg=""):
    print(f"  OK  {msg}")

def fail(msg):
    print(f"\n  FAIL: {msg}")
    print("\nPress Enter to exit...")
    input()
    sys.exit(1)


def main():
    print()
    print(SEP)
    print("   Allegro AI - Network Troubleshooting")
    print(SEP)

    # ── 1. Check Python version ──────────────────────
    step(1, "Checking Python")
    vi = sys.version_info
    if vi < (3, 11):
        fail(f"Python 3.11+ required, you have {vi.major}.{vi.minor}. "
             "Please install from https://www.python.org/downloads/")
    ok(f"Python {vi.major}.{vi.minor}.{vi.micro}")

    # ── 2. Create virtualenv ─────────────────────────
    step(2, "Setting up virtual environment")
    os.chdir(APP_DIR)

    if not VENV_PY.exists():
        print("  Creating venv (first run only, ~30 seconds)...")
        r = subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)])
        if r.returncode != 0:
            fail("Cannot create virtual environment. Try running as Administrator.")
    ok("Virtual environment ready")

    # ── 3. Install packages ──────────────────────────
    step(3, "Installing packages")

    # Upgrade pip silently
    subprocess.run(
        [str(VENV_PY), "-m", "pip", "install", "--upgrade", "pip", "-q"],
        capture_output=True
    )

    req = APP_DIR / "requirements.txt"
    print("  Installing packages (first run may take 1-2 minutes)...")
    r = subprocess.run([str(VENV_PY), "-m", "pip", "install", "-r", str(req), "-q"])
    if r.returncode != 0:
        print("  First attempt failed, retrying with verbose output:")
        r2 = subprocess.run([str(VENV_PY), "-m", "pip", "install", "-r", str(req)])
        if r2.returncode != 0:
            fail("Package installation failed. Check internet connection and try again.")
    ok("Packages ready")

    # ── 4. Create .env.local if missing ─────────────
    env_file = APP_DIR / ".env.local"
    if not env_file.exists():
        env_file.write_text("GEMINI_API_KEY=\n", encoding="utf-8")
        print("  Created .env.local")

    # ── 5. Start server ──────────────────────────────
    step(4, "Starting server")
    print()
    print(SEP)
    print("  Browser will open automatically at:")
    print("  http://localhost:8000")
    print()
    print("  To stop: press Ctrl+C")
    print(SEP)
    print()

    r = subprocess.run([str(VENV_PY), str(APP_DIR / "app.py")])
    if r.returncode != 0:
        fail(f"Server exited with code {r.returncode}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nStopped.")
    finally:
        print("\nPress Enter to exit...")
        input()
