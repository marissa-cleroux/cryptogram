from urllib.request import Request, urlopen
from html.parser import HTMLParser
import re
import random


class Cryptogram:
    def __init__(self, quotes):
        self.quote = self._get_random_quote(quotes)
        self.key = self.randomize_key()
        self.encoded_quote = self._encode_quote()

    def _get_random_quote(self, quotes):
        num = random.randint(0, len(quotes))
        return quotes[num].lower()

    def _encode_quote(self):
        return "".join([self.key[ord(letter) - 97] if letter.isalpha() else letter for letter in self.quote])

    @staticmethod
    def randomize_key():
        alphabet = list(map(chr, range(97, 123)))
        random.shuffle(alphabet)
        return alphabet


class MyHTMLParser(HTMLParser):
    quotes = list()
    is_quote = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'wp_quotepage_quote':
            self.is_quote = True

    def handle_endtag(self, tag):
        if self.is_quote:
            self.is_quote = False

    def handle_data(self, data):
        if self.is_quote:
            m = re.match('^[0-9]*[.] ', data)
            if m:
                self.quotes.append(data[m.end(0):])


url = 'https://litemind.com/best-famous-quotes/'

parser = MyHTMLParser()
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})


with urlopen(req) as f:
    page_one = list(line.decode("utf-8").strip() for line in f.readlines())


for eachline in page_one:
    parser.feed(eachline)


game = Cryptogram(parser.quotes)
print(game.encoded_quote)
print(game.key)
print(game.quote)

