import os
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def parse_file(filepath):
    """Parses a file to extract blocks and connections."""
    blocks = []
    connections = []
    with open(filepath, 'r') as file:
        lines = file.readlines()
        parsing_blocks = True
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if "Blocks:" in line:
                parsing_blocks = True
                continue
            if "Connections:" in line:
                parsing_blocks = False
                continue

            if parsing_blocks:
                parts = line.split(',')
                name = parts[0].strip()
                width = float(parts[1].strip())  # Allow float values
                height = float(parts[2].strip())  # Allow float values
                power = None if parts[3].strip() == 'None' else float(parts[3].strip())
                blocks.append((name, width, height, power))
            else:
                connections.append(line.split())

    return blocks, connections

def analyze_and_visualize(input_dir, output_dir):
    """Analyzes files in the input directory and generates visualizations in the output directory."""
    os.makedirs(output_dir, exist_ok=True)
    
    block_data = []
    connection_counts = []

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        if os.path.isfile(filepath):
            blocks, connections = parse_file(filepath)
            
            # Analyze Blocks
            for name, width, height, power in blocks:
                aspect_ratio = width / height
                block_data.append((name, width, height, aspect_ratio, power))

            # Analyze Connections
            if connections:
                connection_counts.append(len(connections))
                avg_connections = [len(conn) for conn in connections]
                connection_counts.extend(avg_connections)

    # Convert block data to DataFrame
    block_df = pd.DataFrame(block_data, columns=["Name", "Width", "Height", "Aspect Ratio", "Power"])
    
    # Histograms for Width, Height, Aspect Ratio, and Power
    for column in ["Width", "Height", "Aspect Ratio", "Power"]:
        plt.figure()
        data = block_df[column].dropna()
        plt.hist(data, bins=20, alpha=0.7, color='blue', edgecolor='black')
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, f"{column.lower()}_histogram.png"))
        plt.close()

    # Whisker plot for Connection Counts
    if connection_counts:
        plt.figure()
        plt.boxplot(connection_counts, vert=False, patch_artist=True)
        plt.title("Whisker Plot of Connection Counts")
        plt.xlabel("Number of Connections")
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, "connection_counts_whisker_plot.png"))
        plt.close()

    # Box plot for Connections Per Connection
    if connection_counts:
        plt.figure()
        plt.boxplot(connection_counts, patch_artist=True)
        plt.title("Box Plot of Average Connections")
        plt.ylabel("Number of Connections")
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, "connections_per_connection_box_plot.png"))
        plt.close()

    # Create summary statistics file
    summary_stats = {}

    for column in ["Width", "Power", "Aspect Ratio"]:
        data = block_df[column].dropna()
        summary_stats[column] = {
            "Average": data.mean(),
            "1st Quartile": data.quantile(0.25),
            "3rd Quartile": data.quantile(0.75),
            "Median": data.median()
        }
    
    # Save statistics to a text file
    stats_file = os.path.join(output_dir, "summary_statistics.txt")
    with open(stats_file, 'w') as f:
        for column, stats in summary_stats.items():
            f.write(f"{column}:\n")
            for stat, value in stats.items():
                f.write(f"  {stat}: {value:.2f}\n")
            f.write("\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Analyze and visualize block and connection data.")
    parser.add_argument("input_dir", type=str, help="Path to the directory containing input files.")
    parser.add_argument("output_dir", type=str, help="Path to the directory where output plots will be saved.")
    args = parser.parse_args()

    analyze_and_visualize(args.input_dir, args.output_dir)
