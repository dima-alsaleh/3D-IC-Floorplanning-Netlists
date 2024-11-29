import os
import shutil

def remove_duplicates(source_dir, target_dir):
    """
    Removes duplicate files based on their base names (before '.' or '_').
    Only one copy of each duplicate is saved in the target directory.

    Args:
        source_dir (str): The directory to scan for files.
        target_dir (str): The directory to save unique files.
    """
    if not os.path.exists(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Dictionary to track unique base names
    unique_files = {}

    # Walk through the source directory
    for root, _, files in os.walk(source_dir):
        for file in files:
            # Extract the base name (before '.' or '_')
            base_name = file.split('.')[0].split('_')[0]
            if base_name not in unique_files:
                unique_files[base_name] = os.path.join(root, file)
    
    # Copy unique files to the target directory
    for base_name, file_path in unique_files.items():
        shutil.copy(file_path, os.path.join(target_dir, os.path.basename(file_path)))

    print(f"Unique files copied to {target_dir}")

if __name__ == "__main__":
    # Input and output directories
    source_directory = r"C:\Users\Admin\Desktop\ECSE 689\d3\3D-IC-Floorplanning-Netlists\extracted_data"
    target_directory = os.path.join(os.path.dirname(source_directory), "extracted data duplicates removed")

    # Remove duplicates
    remove_duplicates(source_directory, target_directory)
