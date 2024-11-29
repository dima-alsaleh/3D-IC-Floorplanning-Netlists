import requests
import os
import argparse

# URL to the raw file on GitHub
file_url = "https://raw.githubusercontent.com/google-research/circuit_training/main/circuit_training/environment/test_data/simple_with_coords/netlist.pb.txt"






parser = argparse.ArgumentParser(description="Specify the output directory for the downloaded file.")
parser.add_argument("output_dir", help="Target directory to save the file")
args = parser.parse_args()

# Target directory from terminal argument
target_directory = args.output_dir
os.makedirs(target_directory, exist_ok=True)


# File name
file_name = "DeepMind_data.txt"

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
