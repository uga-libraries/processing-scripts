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
        tests = ['error_missing_manifest', 'match_multiple', 'match_single', 'mismatch_fixity_change',
                 'mismatch_name_change']
        for test in tests:
            report = os.path.join('tests', 'accession_aip_comparison', test, 'aip_fixity_changes.csv')
            if os.path.exists(report):
                os.remove(report)

    def test_error_missing_manifest(self):
        """Test for when there are two accessions but one has a bag named incorrectly, so the manifest is not read"""
        # Makes variables for the script arguments and runs the script.
        collection_folder = os.path.join('tests', 'accession_aip_comparison', 'error_missing_manifest', 'collection')
        aips_directory = os.path.join('tests', 'accession_aip_comparison', 'error_missing_manifest', 'aips_dir')
        message = subprocess.run(f'python accession-aip-comparison.py {collection_folder} {aips_directory}',
                                 shell=True, stdout=subprocess.PIPE)

        # Tests the correct message is printed.
        result = message.stdout.decode('utf-8')
        expected = ("tests\\accession_aip_comparison\\error_missing_manifest\\collection\\coll-no-acc-num\\"
                    "coll-no-acc-num_bag\\manifest-md5.txt not found\r\n")
        self.assertEqual(expected, result, "Problem with test for error_missing_manifest, print")

        # Tests the comparison report has the expected content.
        report = os.path.join('tests', 'accession_aip_comparison', 'error_missing_manifest', 'aip_fixity_changes.csv')
        result = csv_to_list(report)
        expected = [['MD5', 'Path', 'Filename'],
                    ['4c144555d6eb4b68b964877f75826212', 'objects/LETTERS/00000005.pdf', '00000005.pdf'],
                    ['d0bf26776c45ba85ac8b758fb7bda269', 'objects/LETTERS/00000001.pdf', '00000001.pdf'],
                    ['e14e77fd155e31088b9e73901aceb31d', 'objects/LETTERS/00000004.pdf', '00000004.pdf']]
        self.assertEqual(expected, result, "Problem with test for error_missing_manifest, report")

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

    def test_mismatch_fixity_change(self):
        """Test for when there are two accessions, two AIPs, and the fixity has changed for 2 AIP file"""
        # Makes variables for the script arguments and runs the script.
        collection_folder = os.path.join('tests', 'accession_aip_comparison', 'mismatch_fixity_change', 'collection')
        aips_directory = os.path.join('tests', 'accession_aip_comparison', 'mismatch_fixity_change', 'aips_dir')
        subprocess.run(f'python accession-aip-comparison.py {collection_folder} {aips_directory}', shell=True)

        # Tests the comparison report has the expected content.
        report = os.path.join('tests', 'accession_aip_comparison', 'mismatch_fixity_change', 'aip_fixity_changes.csv')
        result = csv_to_list(report)
        expected = [['MD5', 'Path', 'Filename'],
                    ['0xx000000xx0x0xxxx000x000x0x0000', 'objects/LETTERS/00000002.pdf', '00000002.pdf'],
                    ['hhhhhhhhhmmmmmmmmmmmmmmmmmmmmmmm', 'objects/LETTERS/00000004.pdf', '00000004.pdf']]
        self.assertEqual(expected, result, "Problem with test for mismatch_fixity_change")

    def test_mismatch_name_change(self):
        """Test for when there is one accession, one AIP, and the MD5 matches but the filename does not"""
        # Makes variables for the script arguments and runs the script.
        collection_folder = os.path.join('tests', 'accession_aip_comparison', 'mismatch_name_change', 'collection')
        aips_directory = os.path.join('tests', 'accession_aip_comparison', 'mismatch_name_change', 'aips_dir')
        subprocess.run(f'python accession-aip-comparison.py {collection_folder} {aips_directory}', shell=True)

        # Tests the comparison report has the expected content.
        report = os.path.join('tests', 'accession_aip_comparison', 'mismatch_name_change', 'aip_fixity_changes.csv')
        result = csv_to_list(report)
        expected = [['MD5', 'Path', 'Filename'],
                    ["d0bf26776c45ba85ac8b758fb7bda269", "objects/LETTERS/'quote'.pdf", "'quote'.pdf"]]
        self.assertEqual(expected, result, "Problem with test for mismatch_name_change")

if __name__ == '__main__':
    unittest.main()
