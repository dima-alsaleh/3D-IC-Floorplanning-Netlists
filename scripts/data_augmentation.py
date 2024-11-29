import os
import random

# Statistics
width_avg = 132.17
width_q1 = 23.00
width_q3 = 44.00
width_med = 34.00

power_avg = 0.46
power_q1 = 0.01
power_q3 = 0.07
power_med = 0.02

aspect_ratio_avg = 1.22
aspect_ratio_q1 = 0.68
aspect_ratio_q3 = 1.54
aspect_ratio_med = 1.00

def generate_block_name(index):
    return f"bk{index}"

def generate_block_data():
    # Generate realistic dimensions and power within the range
    width = random.uniform(width_q1, width_q3)
    height = width * random.uniform(aspect_ratio_q1, aspect_ratio_q3)
    power = random.uniform(power_q1, power_q3)
    return f"{generate_block_name(random.randint(1, 999))}, {int(width)}, {int(height)}, {round(power, 2)}"

def generate_connection_name(index):
    return f"C_{index}"

def generate_connection_data(num_blocks):
    net_name = generate_connection_name(random.randint(0, num_blocks))
    connected_blocks = " ".join(
        generate_block_name(random.randint(1, num_blocks)) for _ in range(random.randint(2, 10))
    )
    return f"{net_name} {connected_blocks};"

def generate_file_content(num_blocks):
    content = ["Blocks:"]
    for _ in range(num_blocks):
        content.append(generate_block_data())

    num_connections = random.randint(10, 50)
    content.append("\nConnections:")
    for i in range(num_connections):
        content.append(generate_connection_data(num_blocks))

    return "\n".join(content)

def main(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for i in range(50):
        file_name = os.path.join(output_dir, f"generated_netlist_{i+1}.txt")
        num_blocks = random.randint(30, 300)
        file_content = generate_file_content(num_blocks)
        with open(file_name, "w") as f:
            f.write(file_content)
    print(f"Generated 50 files in {output_dir}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate test files.")
    parser.add_argument("output_path", type=str, help="Output directory for the files.")
    args = parser.parse_args()
    main(args.output_path)
