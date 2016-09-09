import os
import configparser
import sys


class Console:
    QUIT = "\quit"
    SHOW = '\show'
    END = '\033[0m'
    WHITE = '\033[97m'
    YELLOW = '\033[33m'
    LIGHT_YELLOW = '\033[93m'


class System:
    is_save_to_file = False
    config = None
    config_file = "config/settings.conf"
    file_name = "ytr-words.txt"
    save_path = ""

    def __init__(self, config_file_name=config_file):
        self.config_file = config_file_name
        self.read_config_file()

    def read_config_file(self):
        try:
            config = configparser.ConfigParser()
            if os.path.exists(self.config_file):
                config.read(self.config_file)
                self.save_path = config['save_params']['save_dir']
                self.is_save_to_file = config['save_params']['save_to_file']
                self.file_name = config['save_params']['save_file_name']

                self.config = config
                return config
        except OSError:
            print('Cannot read settings file')
            sys.exit()
        except configparser.Error:
            print('Cannot read settings params')
            sys.exit()

    def save_to_file(self, word, tr_word):
        path = os.path.expanduser("~")
        if os.path.exists(self.save_path):
            path = self.save_path

        with open(path + "/" + self.file_name, "a") as file:
            file.write(word + " - " + tr_word + "\n")
            file.close()

