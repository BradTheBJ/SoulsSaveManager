# Souls Save Manager (Revived)

IMPORTANT: Why Windows may flag this as a virus — and why it isn't one

- Why Windows (SmartScreen / Defender) can flag this:
  - The prebuilt executable is unsigned and unknown to Microsoft; SmartScreen will warn for unknown unsigned apps.
  - Packaging tools (PyInstaller, UPX, etc.) and single-file executables often trigger heuristic detections.
  - The program performs file operations (copying/restoring files under `%APPDATA%`), which can look like suspicious behavior to heuristics.
  - If you distribute a binary rarely seen in the wild, antivirus systems may label it as "potentially unwanted" until it's widely used.

- Why this project is NOT a virus:
  - The project is open-source; all source code is in this repository and can be inspected before running.
  - It does not perform network communication or remote commands — it only copies, restores, and deletes local game save files.
  - No hidden persistence, no background services, no obfuscation, and no data exfiltration logic.
  - The config is a simple local JSON file storing the chosen backup folder; nothing is uploaded or shared.

- How to verify and reduce alerts:
  - Inspect the source code (`main.py`) before running.
  - Build the executable yourself from source (no third-party binary) and run that.
  - Scan the binary or built files with multiple AV engines (VirusTotal) to double-check.
  - If you trust the tool, you can add the binary or the backup folder to your real-time-exclusion list in Windows Defender.
  - For distribution, signing the executable reduces SmartScreen warnings.

---

A simple Python GUI tool to back up and restore FromSoftware game save files.  
Originally a personal project, it was abandoned and later revived for general use.  
It supports **Dark Souls 3, Dark Souls 2, Elden Ring, and Sekiro**.

> ⚠️ **Windows only** — this tool uses `%APPDATA%` paths to locate save files.

---

## Features

- Detects game save files automatically under `%APPDATA%`  
- Backup save files to a user-selected folder  
- Restore backed-up saves to the original location  
- Delete backup folders safely  
- Shows the current save file location in the UI  

---

## Why This Project Exists

This project started as a personal tool, was abandoned, and later revived.  
The revival aims to clean up and modernize the code while keeping it simple and functional.

---

## Requirements

- **Windows OS** (because `%APPDATA%` paths are used)  
- Python 3.x  
- `tkinter` (usually included with Python on Windows)  

> ⚠️ It is recommended to use the **prebuilt binary** for convenience, but you can also run the Python code directly.

---

## Installation & Running

### Option 1: Use Prebuilt Binary (Recommended)

1. Download the prebuilt executable from the [releases page](https://github.com/<your-username>/SaveBackupManager/releases).  
2. Run `souls-save-manager.exe`.  

### Option 2: Run from Source (No Binary Needed)

1. Clone the repository:
   ```bash
   git clone https://github.com/BradTheBJ/SoulsSaveManager.git
   cd SoulsSaveManager

    Run the Python script:

    python souls-save-manager.py
    # You can also use python3 if required

This project is licensed under the **GPLv3**. See the [LICENSE](LICENSE) file for details.
