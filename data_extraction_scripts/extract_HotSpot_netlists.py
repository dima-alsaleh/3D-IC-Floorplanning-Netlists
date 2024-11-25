import os
import sys

def parse_desc_file(desc_file_path):
    blocks = []
    connections = []
    with open(desc_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            # Parsing blocks
            if len(parts) == 5:
                block_name = parts[0]
                area = float(parts[1]) * 1e12  # Convert m^2 to micrometers^2
                min_aspect = float(parts[2])
                max_aspect = float(parts[3])
                width = round((area / min_aspect) ** 0.5)  # Round to nearest integer
                height = round(area / width)  # Round to nearest integer
                blocks.append((block_name, width, height))
            # Parsing connections
            elif len(parts) == 3:
                unit1 = parts[0]
                unit2 = parts[1]
                connections.append((unit1, unit2))
    return blocks, connections

def parse_power_file(power_file_path):
    power_map = {}
    with open(power_file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                block_name = parts[0]
                power = float(parts[1])
                power_map[block_name] = power
    return power_map

def generate_output_file(output_path, blocks, connections, power_map):
    with open(output_path, 'w') as file:
        # Write Blocks section
        file.write("Blocks:\n")
        for block in blocks:
            block_name, width, height = block
            power = power_map.get(block_name, 0)  # Default to 0 if not in power_map
            file.write(f"{block_name}, {width}, {height}, {power}\n")

        # Write Connections section
        file.write("\nConnections:\n")
        for i, connection in enumerate(connections):
            file.write(f"c_{i} {connection[0]} {connection[1]}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_directory> <output_directory>")
        return
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    desc_file = os.path.join(input_dir, "ev6.desc")
    power_file = os.path.join(input_dir, "avg.p")
    output_file = os.path.join(output_dir, "HotSpot_floorplan.txt")

    if not os.path.exists(desc_file):
        print(f"Error: {desc_file} does not exist.")
        return

    if not os.path.exists(power_file):
        print(f"Error: {power_file} does not exist.")
        return

    os.makedirs(output_dir, exist_ok=True)

    blocks, connections = parse_desc_file(desc_file)
    power_map = parse_power_file(power_file)
    generate_output_file(output_file, blocks, connections, power_map)
    print(f"Output written to {output_file}")

if __name__ == "__main__":
    main()
