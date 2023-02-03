# программа находит таблицу на стайте http://wiki.gt/bin/view/ и загружает ее в xls

from Read_HTML_table import Adventure_time, input_config
import json

def start():
    with open('config.json', 'r') as f:
        data = json.load(f)
    data = input_config(data)

    log = data['login']
    pas = data['password']
    url = data['url']
    pattern_name = data['pattern_name']
    save_name = data['save_name']
    number_table = data['number_table']

    exemplar = Adventure_time()
    if exemplar.registration_and_load_HTML(url=url, login=log, password=pas):
        exemplar.parse_HTML(number_table)
        exemplar.save_xslx(pattern_name, save_name)

if __name__ == '__main__':
    start()

