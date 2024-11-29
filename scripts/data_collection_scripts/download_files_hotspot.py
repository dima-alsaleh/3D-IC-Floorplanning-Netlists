import requests
import os
import argparse
# GitHub API URL for the folder
api_url = "https://api.github.com/repos/uvahotspot/HotSpot/contents/examples/example6"
base_raw_url = "https://raw.githubusercontent.com/uvahotspot/HotSpot/master/examples/example6/"

# Target directory
parser = argparse.ArgumentParser(description="Specify the output directory for downloaded files.")
parser.add_argument("output_dir", help="Target directory to save files")
args = parser.parse_args()

target_directory = args.output_dir
os.makedirs(target_directory, exist_ok=True)

print(f"Target directory is set to: {target_directory}")

try:
    # Fetch the file list from GitHub API
    response = requests.get(api_url)
    
    if response.status_code == 200:
        files = response.json()
        if not files:
            print("No files found in the folder.")
            exit()

        # Download each file from the list
        for file in files:
            file_name = file["name"]
            if file["type"] == "file":  # Only download actual files, not directories
                file_url = file["download_url"]
                print(f"Downloading {file_name} from {file_url}")
                
                # Download the file
                file_response = requests.get(file_url)
                if file_response.status_code == 200:
                    # Save the file to the target directory
                    target_path = os.path.join(target_directory, file_name)
                    with open(target_path, "wb") as f:
                        f.write(file_response.content)
                    print(f"Successfully downloaded and saved: {file_name}")
                else:
                    print(f"Failed to download {file_name}. HTTP Status: {file_response.status_code}")
            else:
                print(f"Skipping directory: {file_name}")
    else:
        print(f"Failed to access the GitHub API. HTTP Status: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
