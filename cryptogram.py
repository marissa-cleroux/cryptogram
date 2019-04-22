from urllib.request import Request, urlopen
from html.parser import HTMLParser
import re
import random


class Cryptogram:
    WIN = 1
    ERROR = -1
    STILL_PLAYING = 0

    def __init__(self):
        self.quotes = self.get_quotes()
        self.quote = self._get_random_quote()
        self.key = self.randomize_key()
        self.encoded_quote = self._encode_quote()
        self.guessed = self._get_empty_guessed()
        self.user_cryptogram = [' ' for i in self.encoded_quote]

    def __str__(self):
        pass

    def __eq__(self, obj):
        pass

    def __invert__(self):
        return {ind: [letter, self.encoded_quote[ind]] for ind, letter in enumerate(self.user_cryptogram)}

    @staticmethod
    def get_quotes():
        url = 'https://litemind.com/best-famous-quotes/'

        parser = MyHTMLParser()
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        with urlopen(req) as f:
            page_one = list(line.decode("utf-8").strip() for line in f.readlines())

        for eachline in page_one:
            parser.feed(eachline)

        return parser.quotes

    def _get_random_quote(self):
        num = random.randint(0, len(self.quotes))
        return self.quotes[num].upper()

    @staticmethod
    def randomize_key():
        alphabet = list(map(chr, range(65, 91)))
        random.shuffle(alphabet)
        return alphabet

    def _encode_quote(self):
        return "".join([self.key[ord(letter) - 65] if letter.isalpha() else letter for letter in self.quote])

    def _get_empty_guessed(self):
        return {letter: ' ' for letter in self.key}

    def guess_letter(self, change_val, enter_val):
        if self._validate_letter(enter_val):
            self._change_letter(change_val, enter_val)
            if self._check_for_win():
                return self.WIN
            else:
                return self.STILL_PLAYING
        else:
            return self.ERROR

    @staticmethod
    def _validate_letter(enter_val):
        return bool(re.match('^[A-Za-z]$', enter_val))

    def _change_letter(self, change_val, enter_val):
        self.guessed[change_val] = enter_val
        self.user_cryptogram = [self.guessed[letter] if letter.isalpha() else letter for letter in self.encoded_quote]

    def _check_for_win(self):
        return self.user_cryptogram == self.quote


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

