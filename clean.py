import enchant
import progressbar
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('*'),' (',
           progressbar.ETA(), ') ',
          ]

usd = enchant.Dict('en_US')
gbd = enchant.Dict('en_GB')
stop_words = set(stopwords.words('english'))

keywordFile = open('keywords.txt', 'r')
messyKeywordFile = open('messy.txt', 'a')
cleanedKeywordFile = open('messy_cleaned.txt', 'a')
englishKeywordFile = open('search_EN.txt', 'a')
stopwordsFile = open('stopwords.txt', 'a')

# Reset derived files
open('messy.txt', 'w').write('')
open('search_EN.txt', 'w').write('')
open('messy_cleaned.txt', 'w').write('')
open('stopwords.txt', 'w').write('')

maxRows = 464
count = 0

bar = progressbar.ProgressBar(max_value=maxRows, 
                              widgets=widgets).start()
for line in keywordFile:
  startIndex = line.find('\'')
  endIndex = line.rfind('\'')

  substring = line[startIndex + 1:endIndex]

  word_tokens = word_tokenize(substring)
  filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

  if len(filtered_sentence) == 0:
    stopwordsFile.write(f'{substring}\n')
  elif usd.check(substring) == False and gbd.check(substring) == False:
    messyKeywordFile.write(f'{substring}\n')
    cleanedKeywordFile.write(f'{usd.suggest(substring)}\n')
  else:
    englishKeywordFile.write(f'{substring}\n')

  count = count + 1
  bar.update(1)
