"""
Creates a metadata.csv file for a directory of folders ready to be turned into AIPs.
This file is used as input by the general aip script.
After the script runs, add the title and adjust the version number if not 1.

Parameters:
    aips_directory (required): path to the directory that contains the folders to be made into AIPs
    collection_id (required): collection identifier
    er_number (optional): first sequential number to use for the AIP ID, if not 1
    
Returns:
    metadata.csv created in the aips_directory
"""
import csv
import os
import sys


# Assigns script arguments to variables, including providing default for er_number if no argument provided.
aips_directory = sys.argv[1]
collection_id = sys.argv[2]
try:
    er_number = int(sys.argv[3])
except IndexError:
    er_number = 1

# Calculates the department (ARCHive group) based on the collection id.
# Quits the script with an explanation if it does not match one of the expected patterns.
if collection_id.startswith('harg') or collection_id.startswith('ua'):
    department = 'hargrett'
elif collection_id.startswith('rbrl'):
    department = 'russell'
else:
    print('Collection ID is not an expected pattern. Should start with harg, ua, or rbrl')
    sys.exit(1)

# Creates metadata.csv with a header row in aips_directory.
with open(os.path.join(aips_directory, 'metadata.csv'), 'w', newline='') as md_csv:
    md_write = csv.writer(md_csv)
    md_write.writerow(['Department', 'Collection', 'Folder', 'AIP_ID', 'Title', 'Version'])

    # For each folder in aips_directory, calculates the aip_id and saves row to metadata.csv.
    # All other values are the same for every row.
    for folder_name in os.listdir(aips_directory):
        if folder_name == 'metadata.csv':
            continue
        aip_id = f'{collection_id}-er-{er_number:06}'
        md_write.writerow([department, collection_id, folder_name, aip_id, 'TitleTBD', 1])

        # Adds one to the er_number to be ready for making the next AIP ID.
        er_number += 1
