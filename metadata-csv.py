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

