import json
import os
import time

from odooselenium import TestCase


class TestAccounting(TestCase):
    def test_setup_module(self):
        self.ui.go_to_module('Settings')
        self.ui.install_module('Accounting and Finance', 300)
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'accounting_config.json')
        with open(config_file, 'r') as fp:
            wizard_data = json.load(fp)
        self.ui.wizard_screen(wizard_data[0], 300)
        self.ui.wizard_screen(wizard_data[1], 300)
        time.sleep(20)
