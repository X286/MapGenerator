# coding: utf-8
import configparser
'''
GNU 2.0
Надсройка над configrapcer выполняет те же функции что и оригинал, но
для упрощения некоторые аспекты были убраны.
для получения полного полного списка просто создайте объект и обращайтесь в self.parce
'''
class get_config (object):
    def __init__(self, f_toParce):
        self.parce = configparser.ConfigParser()
        try:
            self.parce.read(f_toParce)
        except:
            raise IOError('Unable to read config file')

    def get_options(self, selection):
        return self.parce.options(selection)

    def get_sections (self):
        return self.parce.sections()

    def set(self, section, options, data):
        self.parce.set(section , options, data)

    def get(self, section, options):
        return self.parce.get(section, options)

    def save(self, filepath):
        try:
            with open(filepath, 'w') as configfile:
                self.parce.write(configfile)
        except:
            raise IOError ('Unable to save config')