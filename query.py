keywords = open('search_ES.txt', 'r', encoding="utf-8")

regex = ''


for line in keywords:
  keyword = line.replace("'", "''").strip().upper()
  regex = '|'.join([regex, f'\\b({keyword})\\b'])


query = f'SELECT COUNT (*) FROM table WHERE REGEXP_LIKE(column, \'{regex}\')'

open('query.sql', 'w', encoding="utf-8").write(query)