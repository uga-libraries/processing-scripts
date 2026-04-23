"""
Create a metadata.csv file for a folder ready to be turned into AIPs.

Parameters:
    pres_copy (required): path to PreservationCopy directory, which contains the folders to be made into AIPs
    coll_id (required): collection identifier
    er_num (optional): first sequential number to use for the AIP ID, if not 1
"""
import csv
import os
import sys


# Variables from script arguments.
pres_copy = sys.argv[1]
coll_id = sys.argv[2]
try:
    er_num = sys.argv[3]
except IndexError:
    er_num = 1

# Calculate department (ARCHive group) based on the collection id.
if coll_id.startswith('harg') or coll_id.startswith('ua'):
    dept = 'hargrett'
elif coll_id.startswith('rbrl'):
    dept = 'russell'
else:
    print('Collection ID is not an expected pattern. Should start with harg, ua, or rbrl')
    sys.exit(1)

# Starts metadata.csv with a header row in pres_copy.
with open(os.path.join(pres_copy, 'metadata.csv'), 'w', newline='') as md:
    md_write = csv.writer(md)
    md_write.writerow(['Department', 'Collection', 'Folder', 'AIP_ID', 'Title', 'Version'])

    # For each folder in pres_dir, calculates aip_id and saves row to metadata.csv.
    # All other values are the same for every row.
    for folder in os.listdir(pres_copy):
        if folder == 'metadata.csv':
            continue
        aip_id = f'{coll_id}-er-{er_num:06}'
        md_write.writerow([dept, coll_id, folder, aip_id, 'TitleTBD', 1])
        er_num += 1
