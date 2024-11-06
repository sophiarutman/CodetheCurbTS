import gzip
import pandas as pd

# Define the path to the .gz file
file_path = 'data/performance_parking_history000.txt.gz'

# Using gzip to read line by line (optional, just for display)
# print("Reading file using gzip:")
# with gzip.open(file_path, 'rt') as f:
#     for line in f:
#         line.strip()  # Process each line as needed

# Using pandas to read the file into a DataFrame
print("\nReading file using pandas:")
try:
    # Adjust sep according to your file's delimiter (e.g., ',', '\t', etc.)
    df = pd.read_csv(file_path, compression='gzip', sep=',')  
    # print(df.head())  # Display the first few rows of the DataFrame

    # Save the DataFrame as a CSV file
    output_file = 'data/parking_data_converted.csv'
    df.to_csv(output_file, index=False)  # Save without the index
    print(f"Data successfully saved to {output_file}")

except Exception as e:
    print("Error reading the file with pandas:", e)




