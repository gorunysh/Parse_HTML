from Read_HTML_table import *

config_name = 'config.json'

exemplar = Adventure_time()
data = open_json(config_name)

# exemplar.registration_and_load_HTML(url=data['url'], login=data['login'], password=data['password'])

# exemplar.parse_HTML(data['number_table'])


# print(exemplar.save_xslx_v4_for_QT(data['pattern_name'], data['save_name']))
exemplar.save_xslx_fontHTML_for_QT(data['save_name'])

# test_print_list(exemplar.parse_HTML('1'))


# open_Excel(data['save_name'])

