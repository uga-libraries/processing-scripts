"""
Adds the DIP access number to the start of every folder title in a directory,
formatted dept-coll#-access-######_folder title

The default is to start the 6-digit sequential number at 1,
but a different number can be included as an optional third argument if there are other access copies.

Parameters:
    access_dir (required): path to the folder with the folders that need to be renamed
    coll (required): collection id, formatted dept-coll#
    id_start (optional): the first sequential number in that folder, if not 1

Returns: None
"""
