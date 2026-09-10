CodeAlpha File Organizer

A simple Python automation tool developed as part of the CodeAlpha Python Programming Internship.

Project Overview

The JPG File Organizer automatically finds .jpg image files inside a selected folder and moves them into a separate JPG_Files folder.

This project demonstrates how Python can be used to automate repetitive file-management tasks.

Features
Accepts a folder path from the user
Checks whether the folder exists
Creates a JPG_Files folder automatically
Finds JPG files
Moves JPG files automatically
Handles .JPG uppercase extensions
Skips duplicate files
Displays the number of files moved
Shows an error for an invalid folder
Technologies Used
Python 3
os
shutil
Project Structure
CodeAlpha_FileOrganizer/
├── file_organizer.py
└── README.md

How to Run

Open the terminal inside the project folder and run:

python file_organizer.py


When the program asks for a folder path, enter the folder you want to organize.

Example:

test_files

Example

Before running:

test_files/
├── photo1.jpg
├── photo2.jpg
└── photo3.jpg


After running:

test_files/
└── JPG_Files/
    ├── photo1.jpg
    ├── photo2.jpg
    └── photo3.jpg

CodeAlpha Task

Task 3 — Task Automation with Python Scripts

This project fulfills the CodeAlpha requirement to automate a real-life repetitive task using Python.

Author

Developed for the CodeAlpha Python Programming Internship.


4. Press **Ctrl + S**.

That's all for now. ✅

Your `README.md` is now documented.

**Don't do anything else yet.** Tell me **"done"** after saving it, and I'll guide you through the next step slowly.