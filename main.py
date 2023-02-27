#!/usr/bin/env python3
# coding=utf-8
#  -*- coding: utf-8 -*-

# программа находит таблицу на стайте http://wiki.gt/bin/view/ и загружает ее в xlsx/xls

from Read_HTML_table import *
from app_from_XWiki_to_xlsx import main_event

qt_or_console = True  # True = QT, False = console
config_name = 'config.json'

def start():
    if qt_or_console:
        main_event(config_name)

    if not qt_or_console:
        try:
            data = open_json(config_name)
        except:
            print('ошибка с файлом json')

    if not qt_or_console:
        exemplar = Adventure_time()
        if exemplar.registration_and_load_HTML(url=data['url'], login=data['login'], password=data['password']):
            try:
                exemplar.parse_HTML(data['number_table'])
            except:
                print('не удалось распарсить HTML')
            try:
                exemplar.save_xslx_V3(data['pattern_name'], data['save_name'])
            except:
                print('Не удалось сохранить файл')

        prob = input('для закрытия программы нажмите Enter')

if __name__ == '__main__':
    start()
