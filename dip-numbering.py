"""
Adds the DIP access number to the start of every folder title in a directory,
formatted dept-coll#-access-######_folder title

The default is to start the 6-digit sequential number at 1,
but a different number can be included as an optional third argument if there are other access copies.

Parameters:
    access_directory (required): path to the folder with the folders that need to be renamed
    collection_id (required): collection id, formatted dept-coll#
    id_start (optional): the first sequential number in that folder, if not 1

Returns: None
"""
import os
import sys


# Assigns required arguments to variables.
access_dir = sys.argv[1]
coll_id = sys.argv[2]

# Calculates the starting sequential number, which is 1 or the value of the optional third argument.
if len(sys.argv) == 4:
    next_num = int(sys.argv[3])
else:
    next_num = 1

# Calculates the access ID for every folder in access_dir and renames the folder to start with it.
for folder in os.listdir(access_dir):
    new_folder = f'{coll_id}-access-{next_num:06d}_{folder}'
    os.rename(os.path.join(access_dir, folder), os.path.join(access_dir, new_folder))
    next_num += 1
    