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
        """Delete the metadata.csv, if made"""
        md_csv = os.path.join(os.getcwd(), 'aips_dir', 'metadata.csv')
        if os.path.exists(md_csv):
            os.remove(md_csv)

    def test_er_number(self):
        """Test for when the er_number is not 1 (default), which also tests the leading zeros added to the AIP ID"""
        # Makes variables for the script arguments and runs the script.
        script_path = os.path.join('..', '..', 'metadata-csv.py')
        aips_directory = os.path.join(os.getcwd(), 'aips_dir')
        subprocess.run(f'python {script_path} {aips_directory} harg-ms123 99')

        # Tests the contents of metadata.csv
        result = csv_to_list(os.path.join(os.getcwd(), 'aips_dir', 'metadata.csv'))
        expected = [['Department', 'Collection', 'Folder', 'AIP_ID', 'Title', 'Version'],
                    ['hargrett', 'harg-ms123', 'Folder #1', 'harg-ms123-er-000099', 'TitleTBD', 1],
                    ['hargrett', 'harg-ms123', 'FolderTitle', 'harg-ms123-er-000100', 'TitleTBD', 1],
                    ['hargrett', 'harg-ms123', 'Folder_A', 'harg-ms123-er-000101', 'TitleTBD', 1]]
        self.assertEqual(expected, result, "Problem with test for er_number")

    def test_harg(self):
        """Test for when the collection id starts with harg"""
        # Makes variables for the script arguments and runs the script.
        script_path = os.path.join('..', '..', 'metadata-csv.py')
        aips_directory = os.path.join(os.getcwd(), 'aips_dir')
        subprocess.run(f'python {script_path} {aips_directory} harg-ms123')

        # Tests the contents of metadata.csv
        result = csv_to_list(os.path.join(os.getcwd(), 'aips_dir', 'metadata.csv'))
        expected = [['Department', 'Collection', 'Folder', 'AIP_ID', 'Title', 'Version'],
                    ['hargrett', 'harg-ms123', 'Folder #1', 'harg-ms123-er-000001', 'TitleTBD', 1],
                    ['hargrett', 'harg-ms123', 'FolderTitle', 'harg-ms123-er-000002', 'TitleTBD', 1],
                    ['hargrett', 'harg-ms123', 'Folder_A', 'harg-ms123-er-000003', 'TitleTBD', 1]]
        self.assertEqual(expected, result, "Problem with test for harg")

    def test_rbrl(self):
        """Test for when the collection id starts with rbrl"""
        # Makes variables for the script arguments and runs the script.
        script_path = os.path.join('..', '..', 'metadata-csv.py')
        aips_directory = os.path.join(os.getcwd(), 'aips_dir')
        subprocess.run(f'python {script_path} {aips_directory} rbrl-999')

        # Tests the contents of metadata.csv
        result = csv_to_list(os.path.join(os.getcwd(), 'aips_dir', 'metadata.csv'))
        expected = [['Department', 'Collection', 'Folder', 'AIP_ID', 'Title', 'Version'],
                    ['russell', 'rbrl-999', 'Folder #1', 'rbrl-999-er-000001', 'TitleTBD', 1],
                    ['russell', 'rbrl-999', 'FolderTitle', 'rbrl-999-er-000002', 'TitleTBD', 1],
                    ['russell', 'rbrl-999', 'Folder_A', 'rbrl-999-er-000003', 'TitleTBD', 1]]
        self.assertEqual(expected, result, "Problem with test for rbrl")

    def test_ua(self):
        """Test for when the collection id starts with ua"""
        # Makes variables for the script arguments and runs the script.
        script_path = os.path.join('..', '..', 'metadata-csv.py')
        aips_directory = os.path.join(os.getcwd(), 'aips_dir')
        subprocess.run(f'python {script_path} {aips_directory} ua12-3456')

        # Tests the contents of metadata.csv
        result = csv_to_list(os.path.join(os.getcwd(), 'aips_dir', 'metadata.csv'))
        expected = [['Department', 'Collection', 'Folder', 'AIP_ID', 'Title', 'Version'],
                    ['hargrett', 'ua12-3456', 'Folder #1', 'ua12-3456-er-000001', 'TitleTBD', 1],
                    ['hargrett', 'ua12-3456', 'FolderTitle', 'ua12-3456-er-000002', 'TitleTBD', 1],
                    ['hargrett', 'ua12-3456', 'Folder_A', 'ua12-3456-er-000003', 'TitleTBD', 1]]
        self.assertEqual(expected, result, "Problem with test for ua")


if __name__ == '__main__':
    unittest.main()
