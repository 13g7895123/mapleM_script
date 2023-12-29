import configparser

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

exe_path = config['path']['exe']
