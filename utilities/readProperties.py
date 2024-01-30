import configparser
import os

config = configparser.RawConfigParser()

# Get the absolute path of the current script/module
current_path = os.path.abspath(__file__)
# Navigate to the parent directory (assuming the configurations folder is at the same level)
project_root = os.path.dirname(os.path.dirname(current_path))
# Construct the full path to config.ini
config_file_path = os.path.join(project_root, 'configurations', 'config.ini')
config.read(config_file_path)
# Print the result
print(config_file_path)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=(config.get('commonInfo', 'baseURL'))
        return url

    @staticmethod
    def getEmail():
        email = (config.get('commonInfo','email'))
        return email

    @staticmethod
    def getPasswd():
        email = (config.get('commonInfo', 'password'))
        return email
