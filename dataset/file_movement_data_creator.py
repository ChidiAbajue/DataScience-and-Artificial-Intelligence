import os
import random
import csv
import time

# Function to generate ordered file name
def generate_ordered_file_name(index):
    return f"file_{index + 1}"

# List of file extensions and their corresponding destination folders
file_destinations = {
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.xls': 'Documents',
    '.xlsx': 'Documents',
    '.ppt': 'Documents',
    '.pptx': 'Documents',
    '.pdf': 'Documents',
    '.txt': 'Documents',
    '.jpg': 'Pictures',
    '.jpeg': 'Pictures',
    '.gif': 'Pictures',
    '.png': 'Pictures',
    '.tif': 'Pictures',
    '.tiff': 'Pictures',
    '.bmp': 'Pictures',
    '.mp3': 'Music',
    '.wma': 'Music',
    '.wav': 'Music',
    '.aac': 'Music',
    '.ogg': 'Music',
    '.avi': 'Videos',
    '.mp4': 'Videos',
    '.mpeg': 'Videos',
    '.wmv': 'Videos',
    '.mov': 'Videos',
    '.mkv': 'Videos',
    '.zip': 'Downloads',
    '.rar': 'Downloads',
    '.7z': 'Downloads',
    '.tar': 'Downloads',
    '.gz': 'Downloads',
    '.exe': 'Downloads',
    '.dll': 'Downloads',
    '.bat': 'Scripts',
    '.py': 'Scripts',
    '.jar': 'Scripts',
    '.html': 'Web',
    '.htm': 'Web',
    '.css': 'Web',
    '.js': 'Web',
    '.php': 'Web',
    '.sh': 'Scripts',
    '.ps1': 'Scripts',
    '.pl': 'Scripts',
    '.dwg': 'CAD',
    '.dxf': 'CAD',
    '.prt': 'CAD',
    '.sldprt': 'CAD',
    '.stp': 'CAD',
    '.dsn': 'CAD',
    '.ipynb': 'Notebooks',
    '.pbix': 'PowerBI'
}

# Function to generate random file size in bytes
def generate_file_size_bytes(file_extension):
    # Limiting file sizes for document and script files to 5MB (5 * 1024 * 1024 bytes)
    if file_extension in ('.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.txt', '.bat', '.py', '.jar', '.sh', '.ps1', '.pl'):
        return random.randint(1, 5 * 1024 * 1024)  # Generating file size between 1 byte and 5MB
    else:
        return random.randint(1, 1000 * 1024)  # Generating file size between 1 byte and 1000KB

# Function to generate random creation and last modified times
def generate_timestamp():
    current_time = time.time()
    creation_time = random.uniform(current_time - 365 * 24 * 60 * 60, current_time)  # Random time within the past year
    modified_time = random.uniform(creation_time, current_time)  # Last modified time is always later than creation time
    return creation_time, modified_time

# Number of samples
num_samples = 150

# Generate dataset
dataset = []
for index in range(num_samples):
    file_extension = random.choice(list(file_destinations.keys()))
    file_name = generate_ordered_file_name(index)
    file_size_bytes = generate_file_size_bytes(file_extension)
    file_size_kb = round(file_size_bytes / 1024, 2)  # Converting bytes to kilobytes and rounding to 2 decimal places
    file_size_mb = round(file_size_kb / 1024, 2)  # Converting kilobytes to megabytes and rounding to 2 decimal places
    creation_time, modified_time = generate_timestamp()
    destination_folder = file_destinations[file_extension]
    dataset.append([file_name, file_extension, file_size_bytes, file_size_kb, file_size_mb, creation_time, modified_time, destination_folder])

# Write dataset to CSV file
csv_file_path = 'file_movement_dataset.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Name', 'File Extension', 'File Size (Bytes)', 'File Size (KB)', 'File Size (MB)', 'File Creation Time', 'Last Modified Time', 'Destination Folder'])
    writer.writerows(dataset)

print(f"Dataset with {num_samples} samples generated successfully and saved as '{csv_file_path}'")
