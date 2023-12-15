import os
import shutil
import tkinter as tk
from tkinter import filedialog

def rename_files_in_directory(directory):
    # List all files
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    # Sort files by creation time
    files.sort(key=lambda x: os.path.getctime(os.path.join(directory, x)))

    # Rename files
    for index, file in enumerate(files, start=1):
        new_file_name = f"{index}{os.path.splitext(file)[1]}"
        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_file_name)
        shutil.move(old_file_path, new_file_path)
        print(f"Renamed '{file}' to '{new_file_name}'")

    print("All files have been renamed successfully.")

def main():
    # Set up Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to choose a directory
    directory = filedialog.askdirectory()
    if directory:
        print(f"Selected Directory: {directory}")
        rename_files_in_directory(directory)
    else:
        print("No directory selected. Exiting...")

if __name__ == "__main__":
    main()
