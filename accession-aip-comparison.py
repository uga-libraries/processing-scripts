"""
Compares the manifests of accession and AIP bags for a processed collection
to find any files in the AIP that were altered during processing
and any files in the accession that were accidentally left out of the AIPs.

Parameters:
    collection_folder: path to the collection folder, which may have one or more accessions
    aips_directory: path to the folder with the bagged, unzipped version of the AIPs

Returns:

"""
import os
import pandas as pd
import sys

if __name__ == '__main__':

    # Assign arguments to variables.
    collection_folder = sys.argv[1]
    aips_directory = sys.argv[2]

    # Find the accession bag manifests in the collection_folder and combine to one dataframe.

    # Find the AIP bag manifests in the aips_directory and combine into one dataframe.

    # Compare the accession and AIP dataframes to find any MD5 that does not occur the same number of times in each.

    # Save the path for every accession and AIP file with MD5s that did not match to a CSV for review.