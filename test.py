from Read_HTML_table import Adventure_time
import json

with open('config.json', 'r') as f:
  data = json.load(f)

log = 'pdemidov'
pas = 'Dmdv_14PV'
# url = 'http://wiki.gt/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/#edit'
url = 'http://wiki.gt/bin/view/07.%20Развитие/ЕЖЕДНЕВНЫЙ%20СТАТУС%20по%20поставщикам/#edit'
pattern_name = 'pattern.xls'
save_name = 'test_save.xls'
number_table = 1

exemplar = Adventure_time()

# if exemplar.registration_and_load_HTML(url=url, login=log, password=pas):
#     exemplar.parse_HTML(number_table)
#     exemplar.save_xslx(pattern_name, save_name)

# if exemplar.registration_and_load_HTML(url=url, login=log, password=pas):

# exemplar.txt_for_test()
# exemplar.test_print_result_no_parse(number_table)

# exemplar.txt_for_test()
# exemplar.parse_HTML(number_table)
# exemplar.save_xslx(pattern_name, save_name)
# exemplar.test_print_HTML()


# exemplar.copy_xls(pattern_name, save_name)

# exemplar.txt_for_test()
# exemplar.parse_HTML2()
