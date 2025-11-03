import os
import shutil

def organize_files(source_folder):
    # File type categories
    file_types = {
        "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
        "Compressed": [".zip", ".rar", ".7z"],
        "Others": []
    }

    # Create destination folders if not present
    for folder in file_types:
        path = os.path.join(source_folder, folder)
        os.makedirs(path, exist_ok=True)

    # Move files to respective folders
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(source_folder, folder, file))
                    print(f"Moved: {file} → {folder}/")
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(source_folder, "Others", file))
                print(f"Moved: {file} → Others/")

    print("\n✅ All files organized successfully!")

if __name__ == "__main__":
    folder_path = input("Enter the folder path to organize: ").strip()
    if os.path.exists(folder_path):
        organize_files(folder_path)
    else:
        print("❌ Invalid path! Please check and try again.")
