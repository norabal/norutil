import unittest
import os

from norutil.definitions import TEST_CONFIG_PATH, ROOT_DIR
from norutil.util import remove_path_if_exists, copy_config_ini_from_sample


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        remove_path_if_exists(TEST_CONFIG_PATH)
        copy_config_ini_from_sample(os.path.join(ROOT_DIR, 'config.ini.sample'), TEST_CONFIG_PATH)

    @classmethod
    def tearDownClass(cls):
        remove_path_if_exists(TEST_CONFIG_PATH)
