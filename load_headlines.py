import csv
import random
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--headline-count", dest="headline_count", type="int",
                  default=10, help="Number of headlines to compare.")

(options, args) = parser.parse_args()

random_headline_index = random.randrange(1103666)
headlines = []

with open('abcnews-date-text.csv', 'r') as file:
    headline_reader = csv.reader(file, delimiter=',')
    raw_headlines = list(headline_reader)[random_headline_index - options.headline_count:random_headline_index]

    for headline in raw_headlines:
        headlines.append(headline[1])
