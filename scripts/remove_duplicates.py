import os
import shutil
import sys

def remove_duplicates(source_dir, target_dir):
    """
    Removes duplicate files based on their base names.
    If the name starts with 'Corblivar', 'SMU', or 'UM', the part before the first '_' is ignored,
    and duplicates are detected using the part of the name between the first '_' and the second '_'
    or the first '.'.

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
            # Extract the relevant part of the name for duplicate detection
            file_name = os.path.basename(file)
            if file_name.startswith(("Corblivar_", "SMU_", "UM_")):
                # Ignore the prefix (before the first '_') and extract the part between the first '_' and second '_' or '.'
                remaining_part = file_name.split('_', 1)[1]
                base_name = remaining_part.split('_')[0].split('.')[0]
            else:
                # Use the part before the first '.' or '_'
                base_name = file_name.split('.')[0].split('_')[0]

            if base_name not in unique_files:
                unique_files[base_name] = os.path.join(root, file)
    
    # Copy unique files to the target directory
    for base_name, file_path in unique_files.items():
        shutil.copy(file_path, os.path.join(target_dir, os.path.basename(file_path)))

    print(f"Unique files copied to {target_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_duplicates.py <source_dir> <target_dir>")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2]

    # Remove duplicates
    remove_duplicates(source_directory, target_directory)
