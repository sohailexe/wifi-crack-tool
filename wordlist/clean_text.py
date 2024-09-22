# Define the input and output file paths
input_file_path = 'worldList.txt'
output_file_path = '2_worldList.txt'

# Define the replacement text
replacement_text = ""

# Open the input file for reading and the output file for writing
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        stripped_line = line.strip()
        # Check if the line length is less than 8 and is not empty
        if len(stripped_line) < 8 and stripped_line:
            output_file.write(replacement_text)  # Replace with the specified text
        elif stripped_line:  # Write original line if it's not empty
            output_file.write(line)

print("Lines shorter than 8 characters have been replaced, and no blank lines were left.")
