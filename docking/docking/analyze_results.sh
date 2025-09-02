#!/bin/bash

# Define the output CSV file name
output_csv="results.csv"

# Clear the old CSV and add the header
echo "ligand_name,affinity_kcal/mol" > "$output_csv"

# Check if the directory exists
if [ ! -d "screening_results" ]; then
    echo "Error: 'screening_results' directory not found."
    exit 1
fi

# Loop through each Vina output file in the directory
for file in screening_results/*.pdbqt; do
    # Check if any files were found
    if [ ! -f "$file" ]; then
        echo "Error: No .pdbqt files found in 'screening_results'."
        exit 1
    fi

    # Extract the ligand name from the filename
    ligand_name=$(basename "$file" .pdbqt)

    # Use grep to find the first line with the Vina result and awk to extract the affinity
    # -m 1 option stops grep after the first match
    affinity=$(grep -m 1 "REMARK VINA RESULT:" "$file" | awk '{print $4}')

    # Append the ligand name and affinity to the CSV file
    echo "$ligand_name,$affinity" >> "$output_csv"
done

echo "CSV file '$output_csv' has been created successfully."
