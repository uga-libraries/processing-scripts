import os
import pandas as pd
import subprocess
import unittest


def csv_to_list(csv_path):
    """Make a list with the rows from the csv for easier comparison"""
    df = pd.read_csv(csv_path)
    csv_list = [df.columns.to_list()] + df.values.tolist()
    return csv_list


class MyTestCase(unittest.TestCase):

    def tearDown(self):
        """Delete the comparison report, if made (should only be made for mismatch tests"""
        tests = ['error_missing_manifests', 'match_multiple', 'match_single', 'mismatch_fixity_change',
                 'mismatch_name_change']
        for test in tests:
            report = os.path.join('tests', 'accession_aip_comparison', test, 'aip_fixity_changes.csv')
            if os.path.exists(report):
                os.remove(report)

    def test_match_multiple(self):
        """Test for when there are two accessions, two AIPs, the accessions include duplicates,
        and all AIP MD5 + filenames match at least one row in the accession"""
        # Makes variables for the script arguments and runs the script.
        collection_folder = os.path.join('tests', 'accession_aip_comparison', 'match_multiple', 'collection')
        aips_directory = os.path.join('tests', 'accession_aip_comparison', 'match_multiple', 'aips_dir')
        message = subprocess.run(f'python accession-aip-comparison.py {collection_folder} {aips_directory}',
                                 shell=True, stdout=subprocess.PIPE)

        # Tests the correct message is printed. It would not print if a report was made.
        result = message.stdout.decode('utf-8')
        expected = "AIP fixity is unchanged\r\n"
        self.assertEqual(expected, result, "Problem with test for match_multiple")

    def test_match_single(self):
        """Test for when there is one accession, one AIP, and all AIP MD5 + filenames match one row in the accession"""
        # Makes variables for the script arguments and runs the script.
        collection_folder = os.path.join('tests', 'accession_aip_comparison', 'match_single', 'collection')
        aips_directory = os.path.join('tests', 'accession_aip_comparison', 'match_single', 'aips_dir')
        message = subprocess.run(f'python accession-aip-comparison.py {collection_folder} {aips_directory}',
                                 shell=True, stdout=subprocess.PIPE)

        # Tests the correct message is printed. It would not print if a report was made.
        result = message.stdout.decode('utf-8')
        expected = "AIP fixity is unchanged\r\n"
        self.assertEqual(expected, result, "Problem with test for match_single")


if __name__ == '__main__':
    unittest.main()
