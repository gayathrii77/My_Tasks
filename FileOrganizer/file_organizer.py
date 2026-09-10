import os
import shutil

print("=" * 50)
print("           JPG FILE ORGANIZER")
print("=" * 50)

# Ask the user for the folder to organize
folder_path = input("Enter the folder path: ").strip()

# Check whether the folder exists
if not os.path.isdir(folder_path):
    print("Error: Folder does not exist.")
    exit()

# Create destination folder
destination = os.path.join(folder_path, "JPG_Files")

if not os.path.exists(destination):
    os.makedirs(destination)

# Find and move JPG files
moved_files = 0

for filename in os.listdir(folder_path):
    source = os.path.join(folder_path, filename)

    if os.path.isfile(source) and filename.lower().endswith(".jpg"):
        target = os.path.join(destination, filename)

        # Avoid moving a file if it already exists in destination
        if os.path.exists(target):
            print(f"Skipped: {filename} already exists.")
            continue

        shutil.move(source, target)
        print(f"Moved: {filename}")
        moved_files += 1

print("\n" + "=" * 50)
print(f"Total JPG files moved: {moved_files}")
print(f"Files are now in: {destination}")
print("=" * 50)
print("File organization completed successfully!")
