import json
from common.constant_path import ConstantPath
import os


class ConfigLoader:

    @staticmethod
    def get_file_conf():
        with open(ConstantPath.CONFIG_FILE_PATH) as json_data_file:
            data = json.load(json_data_file)
            return data

    @staticmethod
    def get_active_environment():
        return ConfigLoader.get_file_conf()['active_environment']

    @staticmethod
    def get_ui_running_conf():
        return ConfigLoader.get_file_conf()['ui_running_config']

    @staticmethod
    def get_ui_env_conf(env):
        return ConfigLoader.get_file_conf()['ui_environments'][env]


class EnvConf:
    ACTIVE_ENV = os.getenv('ACTIVE_ENV', ConfigLoader.get_active_environment())

    UI_RUNNING_CONFIG = ConfigLoader.get_ui_running_conf()
    UI_LANGUAGE = os.getenv('LANG_CONF', UI_RUNNING_CONFIG['ui_language'])
    UI_BROWSER = os.getenv('BROWSER_NAME', UI_RUNNING_CONFIG['ui_browser'])

    UI_ENV_CONF = ConfigLoader.get_ui_env_conf(ACTIVE_ENV)
    OPEN_WEATHER_URL = os.getenv('OPEN_WEATHER_URL', ConfigLoader.get_ui_env_conf(ACTIVE_ENV)['open_weather_url'])
