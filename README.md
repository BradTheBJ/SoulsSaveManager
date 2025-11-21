# Souls Save Manager (Revived)

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
2. Run `SaveBackupManager.exe`.  

### Option 2: Run from Source (No Binary Needed)

1. Clone the repository:
   ```bash
   git clone https://github.com/BradTheBJ/SoulsSaveManager.git
   cd SoulsSaveManager
   ```

2. Run the Python script:
    ```bash
    python souls-save-manager.py
    # You can also use python3 if required    
---
This project is licensed under the **GPLv3**. See the [LICENSE](LICENSE) file for details.

