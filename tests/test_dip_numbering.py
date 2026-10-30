import os
import shutil
import subprocess
import unittest


def dir_list(dir_path):
    """Make a list of the folder names in a directory"""
    folder_list = []
    for folder in os.listdir(dir_path):
        folder_list.append(folder)
    return folder_list


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """Makes a folder with multiple subfolders for test input"""
        os.mkdir('access_dir')
        for folder in ['Apple', 'book_drive', 'Circus Arts']:
            folder_path = os.path.join('access_dir', folder)
            os.mkdir(folder_path)

    def tearDown(self):
        """Delete the test input, which is renamed by the test and must be recreated each time"""
        shutil.rmtree('access_dir')

    def test_default(self):
        """Test for when the sequential number starts at 1 (default behavior, no 3rd argument)"""
        # Runs the script.
        script_path = os.path.join('..', 'dip-numbering.py')
        subprocess.run(f'python {script_path} access_dir harg-ms123')

        # Tests the contents of the access directory.
        result = dir_list('access_dir')
        expected = ['harg-ms123-access-000001_Apple',
                    'harg-ms123-access-000002_book_drive',
                    'harg-ms123-access-000003_Circus Arts']
        self.assertEqual(expected, result, "Problem with test for default")

    def test_id_start(self):
        """Test for when the sequential starting number is provided with the optional 3rd argument"""
        # Runs the script.
        script_path = os.path.join('..', 'dip-numbering.py')
        subprocess.run(f'python {script_path} access_dir rbrl-001 99')

        # Tests the contents of the access directory.
        result = dir_list('access_dir')
        expected = ['rbrl-001-access-000099_Apple',
                    'rbrl-001-access-000100_book_drive',
                    'rbrl-001-access-000101_Circus Arts']
        self.assertEqual(expected, result, "Problem with test for id_start")


if __name__ == '__main__':
    unittest.main()
