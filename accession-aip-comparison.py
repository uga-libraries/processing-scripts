"""
Compares the filename and MD5 from the AIP bag manifests to the accession manifests for a processed collection
to find any files in the AIP that were altered during processing.

The filename is included in the match to remove the risk of an MD5 collision between two files,
but the file path is not used since folders may be moved or renamed.
This will identify any renamed files as a fixity change, but these are rare.

Parameters:
    collection_folder: path to the collection folder, which may have one or more accessions
    aips_directory: path to the folder with the bagged, unzipped version of the AIPs

Returns:
    aip_fixity_changes.csv: report with the MD5 and filepath of any AIP file that didn't match the accession

"""
import os
import pandas as pd
import sys


def accession_manifests(coll_folder):
    """Find every accession bag manifest in the collection folder and combine to one df"""
    df_combined = pd.DataFrame(columns=['MD5', 'Path'])
    for folder_name in os.listdir(coll_folder):
        if folder_name.lower().endswith('er') or folder_name.endswith('no-acc-num'):
            manifest_path = os.path.join(coll_folder, folder_name, f'{folder_name}_bag', 'manifest-md5.txt')
            try:
                df = pd.read_csv(manifest_path, delimiter='  data/', engine='python', header=None, names=['MD5', 'Path'])
                df_combined = pd.concat([df_combined, df], ignore_index=True)
            except FileNotFoundError:
                print(f'{manifest_path} not found')

    # Add a column with just the filename.
    df_combined['Filename'] = df_combined['Path'].str.split('/').str[-1]

    return df_combined


if __name__ == '__main__':

    # Assign arguments to variables and calculate parent of aips_directory for saving the report.
    collection_folder = sys.argv[1]
    aips_directory = sys.argv[2]
    output_directory = os.path.dirname(aips_directory)

    # Find the accession bag manifests in the collection_folder and combine to one dataframe.
    df_accession = accession_manifests(collection_folder)

    # Find the AIP bag manifests in the aips_directory and combine into one dataframe.

    # Compare the accession and AIP dataframes to find any MD5 that does not occur the same number of times in each.

    # Save the path for every accession and AIP file with MD5s that did not match to a CSV for review.