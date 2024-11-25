import sys
import os
import re

def parse_netlist(input_dir, output_dir):
    # Locate input file in the directory
    input_file = os.path.join(input_dir, "netlist.pb.txt")
    if not os.path.isfile(input_file):
        print(f"Error: The file 'netlist.pb.txt' was not found in the directory {input_dir}")
        sys.exit(1)

    # Ensure output directory exists
    if not os.path.isdir(output_dir):
        print(f"Error: The output directory {output_dir} does not exist.")
        sys.exit(1)

    # Define output file path
    output_file = os.path.join(output_dir, "DeepMind_floorplan.txt")

    with open(input_file, 'r') as f:
        content = f.read()
    
    # Regex to find nodes with width and height
    block_pattern = re.compile(
        r'node\s*{\s*name:\s*"(?P<name>.*?)".*?'
        r'attr\s*{\s*key:\s*"width".*?f:\s*(?P<width>[\d.]+).*?'
        r'attr\s*{\s*key:\s*"height".*?f:\s*(?P<height>[\d.]+).*?}', 
        re.DOTALL
    )

    blocks = []

    # Extract blocks
    for match in block_pattern.finditer(content):
        name = match.group("name")
        width = match.group("width")
        height = match.group("height")
        blocks.append(f"{name}, {width}, {height}, None")

    # Write to output file
    with open(output_file, 'w') as f:
        f.write("Blocks:\n")
        f.write("\n".join(blocks))
        f.write("\n\nConnections:\n")  # Connections remain empty

    print(f"Output written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_directory> <output_directory>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    parse_netlist(input_dir, output_dir)
