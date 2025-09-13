import pandas as pd
from pathlib import Path

def extract_first_column(csv_file_path, output_file="first_column.txt"):
    """
    Extract all data from the first column of a CSV file to a text file
    
    Args:
        csv_file_path (str): Path to the CSV file
        output_file (str): Name of the output text file
    """
    try:
        # Load CSV
        df = pd.read_csv(csv_file_path)
        print(f"Loaded CSV: {len(df)} rows, {len(df.columns)} columns")
        
        # Get first column
        first_column = df.iloc[:, 0]  # Get column by position (0 = first)
        column_name = df.columns[0]
        print(f"Extracting column: '{column_name}'")
        
        # Write to text file
        with open(output_file, 'w', encoding='utf-8') as f:
            for value in first_column:
                if pd.notna(value):  # Skip empty values
                    f.write(f"{value}\n")
        
        # Count non-empty values
        word_count = first_column.notna().sum()
        print(f"✓ Created '{output_file}' with {word_count} entries")
        
    except Exception as e:
        print(f"Error: {e}")

# Usage
if __name__ == "__main__":
    extract_first_column(
        "../../../assets/excel_files/10000_most_common_russian_words.csv",
        "../../../assets/text_data/russian_words.txt"
    )
