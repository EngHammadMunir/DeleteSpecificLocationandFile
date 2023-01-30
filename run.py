import os

# Define the file path
file_path = "path/to/file.ext"

# Check if the file exists
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print("File successfully deleted.")
else:
    print("File does not exist.")
