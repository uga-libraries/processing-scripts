"""
Create a metadata.csv file for a folder ready to be turned into AIPs.

Parameters:
    pres_copy (required): path to PreservationCopy directory, which contains the folders to be made into AIPs
    coll_id (required): collection identifier
    start_num (optional): first sequential number to use for the AIP ID, if not 1
"""
import csv
import os
import sys


# Variables from script arguments.
pres_copy = sys.argv[1]
coll_id = sys.argv[2]
try:
    start_num = sys.argv[3]
except IndexError:
    start_num = 1

# Calculate group based on the collection id.
if coll_id.startswith('harg') or coll_id.startswith('ua'):
    group = 'hargrett'
elif coll_id.startswith('rbrl'):
    group = 'russell'
else:
    print('Collection ID is not an expected pattern. Should start with harg, ua, or rbrl')
    sys.exit(1)

