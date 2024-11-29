import re
import os
import sys


def parse_yal_file(file_path):
    """
    Parses a .yal file and extracts blocks and connections.
    """
    blocks = []
    connections_section = ""

    with open(file_path, 'r') as file:
        content = file.read()

    # Extract MODULE blocks
    modules = re.findall(r'MODULE\s+(\S+);(.*?)ENDMODULE;', content, re.DOTALL)

    for module_name, module_content in modules:
        module_name = module_name.strip()

        # Extract dimensions
        dimensions = re.search(r'DIMENSIONS\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)', module_content)
        width, height = None, None
        if dimensions:
            x1, y1, x2, y2, x3, y3 = map(int, dimensions.groups())
            width = abs(x3 - x1)
            height = abs(y3 - y1)

        # Extract power details (Voltage * Current)
        power = []
        io_entries = re.findall(r'(P_\d+)\s+PWR.*?CURRENT\s+([\d\.]+)\s+VOLTAGE\s+([\d\.]+)', module_content)
        for _, current, voltage in io_entries:
            power.append(float(current) * float(voltage))

        blocks.append({
            'name': module_name,
            'width': width,
            'height': height,
            'power': sum(power) if power else None,
        })

        # Extract NETWORK block content
        if "NETWORK;" in module_content:
            network_block = re.search(r'NETWORK;(.*?)ENDNETWORK;', module_content, re.DOTALL)
            if network_block:
                connections_section += network_block.group(1).strip() + "\n"

    return blocks, connections_section.strip()


def format_output(blocks, connections_section):
    """
    Formats parsed blocks and the raw network section into a string.
    """
    output = []

    # Write blocks
    output.append("Blocks:")
    for block in blocks:
        # Skip blocks without dimensions (bound blocks)
        if block['width'] is None or block['height'] is None:
            continue
        power_str = f"{block['power']:.2f}" if block['power'] else 'None'
        output.append(f"{block['name']}, {block['width']}, {block['height']}, {power_str}")

    # Write raw network connections
    output.append("\nConnections:")
    output.append(connections_section)

    return '\n'.join(output)


# Main script functionality
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_SMU_netlists.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        # Process files without an extension
        if '.' not in filename:
            input_path = os.path.join(input_folder, filename)
            # Add the prefix "Corblivar_" to the output file name
            output_path = os.path.join(output_folder, f"Corblivar_{filename}_parsed.txt")

            # Parse and generate output
            blocks, connections = parse_yal_file(input_path)
            output = format_output(blocks, connections)

            # Write to file
            with open(output_path, 'w') as out_file:
                out_file.write(output)

            print(f"Processed {filename} -> {output_path}")
        #else:
            # Skip files with extensions
            #print(f"Skipping {filename} (has an extension)")
