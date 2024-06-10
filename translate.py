import argparse
import progressbar
from deep_translator import GoogleTranslator

widgets = [' [',
  progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
  '] ',
    progressbar.Bar('*'),' (',
    progressbar.ETA(), ') ',
  ]

maxRows = 363
count = 0

bar = progressbar.ProgressBar(max_value=maxRows, 
                              widgets=widgets).start()

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--language', help = "Indicate target language: es, hi, ru, uk, vi")
args = parser.parse_args()

validLanguages = ['es', 'hi', 'ru', 'uk', 'vi']

if args.language == None:
  raise Exception('Missing required option: --language')
elif args.language not in validLanguages:
  raise Exception('Provided language is not supported')

targetLanguage = args.language

print(f'Translating to language: {args.language}')

def setupFile(language):
  filename = f'search_{language.upper()}.txt'
  open(filename, 'w', encoding="utf-8").write('')
  return open(filename, 'a', encoding="utf-8")

def setupTranslator(language):
  return GoogleTranslator(source='auto', target=language)

keywordFile = open('cleaned_keywords.txt', 'r')
translatedFile = setupFile(targetLanguage)
translator = setupTranslator(targetLanguage)


for line in keywordFile:
  keyword = line.strip()
  translated = translator.translate(keyword.upper())
  translatedFile.write(f'{translated.upper()}\n')

  count = count + 1
  bar.update(count)
