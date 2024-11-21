import requests
import os

# URL to the raw file on GitHub
file_url = "https://raw.githubusercontent.com/google-research/circuit_training/main/circuit_training/environment/test_data/simple_with_coords/netlist.pb.txt"

# Target directory
target_directory = r"C:\Users\Admin\Desktop\ECSE 689\d3\3D-IC-Floorplanning-Netlists\raw data\DeepMind"
os.makedirs(target_directory, exist_ok=True)

# File name
file_name = os.path.basename(file_url)

print(f"Target directory is set to: {target_directory}")
print(f"Downloading {file_name} from {file_url}")

try:
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

except Exception as e:
    print(f"An error occurred: {e}")
