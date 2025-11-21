import os
import shutil
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import glob
import json

# Paths to game save folders
APPDATA = os.getenv('APPDATA')
PATH_DS3 = os.path.join(APPDATA, 'DarkSoulsIII')
PATH_ELDEN = os.path.join(APPDATA, 'EldenRing')
PATH_DS2 = os.path.join(APPDATA, 'DarkSoulsII')
PATH_SEKIRO = os.path.join(APPDATA, 'Sekiro')

CONFIG_FILE = os.path.join(os.path.expanduser('~'), 'save_manager_config.json')


def load_saved_destination():
    if os.path.exists(CONFIG_FILE):
        return json.load(open(CONFIG_FILE)).get("backup_dir")
    return None


def save_destination(path):
    json.dump({"backup_dir": path}, open(CONFIG_FILE, 'w'))


backup_dir = load_saved_destination()


def find_savefile(game_path, game_name):
    """Find .sl2 savefile (Elden Ring excludes .bak)."""
    pattern = os.path.join(game_path, "**", "*.sl2")
    results = glob.glob(pattern, recursive=True)
    if game_name == "Elden Ring":
        results = [r for r in results if not r.endswith(".sl2.bak")]
    return results[0] if results else None


def get_paths(game_name):
    """Return (save_path, backup_folder_path)."""
    if not backup_dir:
        return None, None

    if game_name == "Dark Souls 3":
        return find_savefile(PATH_DS3, game_name), os.path.join(backup_dir, "DS3_Backup")

    if game_name == "Elden Ring":
        return find_savefile(PATH_ELDEN, game_name), os.path.join(backup_dir, "EldenRing_Backup")

    if game_name == "Dark Souls 2":
        return find_savefile(PATH_DS2, game_name), os.path.join(backup_dir, "DS2_Backup")

    if game_name == "Sekiro":
        return find_savefile(PATH_SEKIRO, game_name), os.path.join(backup_dir, "Sekiro_Backup")

    return None, None


def backup_save():
    game = game_var.get()
    save_path, backup_folder = get_paths(game)

    if not save_path:
        messagebox.showerror("Error", "No save file found.")
        return

    os.makedirs(backup_folder, exist_ok=True)
    dest = os.path.join(backup_folder, os.path.basename(save_path))

    shutil.copyfile(save_path, dest)
    messagebox.showinfo("Backed Up", f"Saved to:\n{dest}")


def restore_save():
    game = game_var.get()
    save_path, backup_folder = get_paths(game)

    if not save_path:
        messagebox.showerror("Error", "Could not locate game save file.")
        return

    backup_file = os.path.join(backup_folder, os.path.basename(save_path))

    if not os.path.exists(backup_file):
        messagebox.showerror("Error", "Backup not found.")
        return

    shutil.copyfile(backup_file, save_path)
    messagebox.showinfo("Restored", f"Restored from:\n{backup_file}")


def delete_backup():
    game = game_var.get()
    _, backup_folder = get_paths(game)

    if not backup_folder or not os.path.exists(backup_folder):
        messagebox.showerror("Error", "Backup folder not found.")
        return

    if messagebox.askyesno("Confirm", "Delete this backup folder?"):
        shutil.rmtree(backup_folder)
        messagebox.showinfo("Deleted", "Backup folder removed.")


def pick_destination():
    global backup_dir

    folder = filedialog.askdirectory()
    if folder:
        backup_dir = folder
        save_destination(folder)
        target_label.config(text=f"Backup Folder: {backup_dir}")


def show_save_location():
    game = game_var.get()
    save_path, _ = get_paths(game)
    found_label.config(text=f"Save Found: {save_path or 'None'}")


def enable_buttons(event):
    backup_btn.config(state=tk.NORMAL)
    restore_btn.config(state=tk.NORMAL)
    delete_btn.config(state=tk.NORMAL)
    show_save_location()


# ---------------- UI ----------------

root = tk.Tk()
root.title("Save Backup Manager")
root.geometry("800x600")

title = tk.Label(root, text="Save File Backup Manager", font=("Helvetica", 18))
title.pack(pady=12)

game_var = tk.StringVar()
game_box = ttk.Combobox(
    root,
    textvariable=game_var,
    values=["Dark Souls 3", "Elden Ring", "Dark Souls 2", "Sekiro"],
    state="readonly",
    font=("Helvetica", 14),
    width=25
)
game_box.set("Select Game")
game_box.bind("<<ComboboxSelected>>", enable_buttons)
game_box.pack(pady=10)

target_label = tk.Label(root, text=f"Backup Folder: {backup_dir or 'Not set'}", font=("Helvetica", 12))
target_label.pack(pady=8)

set_target_btn = tk.Button(root, text="Choose Backup Folder", command=pick_destination, width=30, height=2)
set_target_btn.pack(pady=10)

found_label = tk.Label(root, text="Save Found: None", font=("Helvetica", 11))
found_label.pack(pady=6)

backup_btn = tk.Button(root, text="Backup Save", width=30, height=3, command=backup_save, state=tk.DISABLED)
backup_btn.pack(pady=15)

restore_btn = tk.Button(root, text="Restore Save", width=30, height=3, command=restore_save, state=tk.DISABLED)
restore_btn.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Backup Folder", width=30, height=3, command=delete_backup, state=tk.DISABLED)
delete_btn.pack(pady=10)

if not backup_dir:
    pick_destination()

root.mainloop()
