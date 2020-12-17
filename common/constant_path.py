import os


class ConstantPath:
    CONFIG_FILE_PATH = os.getenv('CONFIG_FILE_PATH', './common/config.json')
