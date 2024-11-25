import os
import sys

def process_file(input_path, output_path):
    """
    Process a single input file and write the formatted data to the output file.
    """
    # Check input file extension
    if not input_path.endswith(".txt") or input_path.endswith(".bbb.txt"):
        print(f"Skipping file: {input_path}")
        return

    try:
        with open(input_path, "r") as infile:
            lines = infile.readlines()
        
        # Read the number of blocks (first line) and ignore it
        num_blocks = lines[0].strip()

        # Process the block details
        blocks = []
        for i, line in enumerate(lines[1:], start=1):
            parts = line.strip().split()
            if len(parts) == 2:  # Ensure it's a valid line with two numbers
                x, y = parts
                blocks.append(f"block{i}, {x}, {y}, None")
        
        # Write to the output file
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as outfile:
            outfile.write("Blocks:\n")
            outfile.write("\n".join(blocks))
        
        print(f"Processed file: {input_path}")
        print(f"Output written to {output_path}")
    
    except Exception as e:
        print(f"Error processing file: {input_path}, Error: {e}")


if __name__ == "__main__":
    """
    Main script entry point.
    Usage: python script.py <input_directory> <output_directory>
    """
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_directory> <output_directory>")
    else:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]

        # Validate input directory
        if not os.path.isdir(input_dir):
            print(f"Invalid input directory: {input_dir}")
        else:
            # Process each file in the input directory
            for file_name in os.listdir(input_dir):
                input_path = os.path.join(input_dir, file_name)
                output_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_processed.txt")
                process_file(input_path, output_path)
