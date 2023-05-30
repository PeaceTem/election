# Specify the input and output file paths
input_file = 'free.sql'
output_file = 'output.sql'

# Read the input file and remove newline characters
with open(input_file, 'r') as file:
    content = file.read().replace('\n', '')

# Save the modified content to the output file
with open(output_file, 'w') as file:
    file.write(content)

print("File processing complete. New file saved as", output_file)
