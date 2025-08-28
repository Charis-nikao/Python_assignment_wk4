# Read and write file content with modification
try:
    # Open the original file for reading
    with open("input.txt", "r") as file:
        content = file.read()

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("output.txt", "w") as file:
        file.write(modified_content)

    print("File has been read and modified content written to 'output.txt'.")

except FileNotFoundError:
    print("Error: 'input.txt' not found. Please check the filename.")
