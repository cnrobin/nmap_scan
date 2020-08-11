#coding:utf-8
import configparser
config=configparser.ConfigParser()
config.read('properties.conf')
lists_header=config.sections()
print(lists_header)
print(config['scan']['ip_file'])
print(config['scan']['temp_dir'])
