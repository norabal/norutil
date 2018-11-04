import unittest

from norutil.config import get_config
from norutil.definitions import TEST_CONFIG_PATH
from norutil.util import remove_path_if_exists, copy_config_ini_from_sample
from tests.base import BaseTest


class ConfigTest(BaseTest):
    def test_if_config_file_not_existed(self):
        remove_path_if_exists(TEST_CONFIG_PATH)
        config = get_config(TEST_CONFIG_PATH)
        self.assertEqual(config.sections(), [])

    def test_read_existing_config_file(self):
        copy_config_ini_from_sample()
        config = get_config(TEST_CONFIG_PATH)
        self.assertEqual(config.sections(), [
            'memo',
            'excel',
            'ssl',
            'twitter'
        ])
        self.assertEqual(config.get('memo', 'memo_dir'), '~/memo')


if __name__ == "__main__":
    unittest.main()
