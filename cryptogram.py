from urllib.request import Request, urlopen
from html.parser import HTMLParser
import re
import random


class Cryptogram:
    def __init__(self):
        self.quotes = self.get_quotes()
        self.quote = None
        self.key = None
        self.encoded_quote = None
        self.guessed = None
        self.user_cryptogram = None
        self.ALPHABET = list(map(chr, range(65, 91)))
        self.WIN = 1
        self.STILL_PLAYING = 0

    def __invert__(self):
        return {ind: [letter, self.encoded_quote[ind]] for ind, letter in enumerate(self.user_cryptogram)}

    def __str__(self):
        guessed = [v for k, v in self.guessed.items() if v != ' ']
        return " ".join(sorted([char for char in self.ALPHABET if char not in guessed]))

    def start_new_game(self):
        self.quote = self._get_random_quote()
        self.key = self.randomize_key()
        self.encoded_quote = self._encode_quote()
        self.guessed = self._get_empty_guessed()
        self.user_cryptogram = [' ' for i in self.encoded_quote]

    @staticmethod
    def get_quotes():
        url = 'https://litemind.com/best-famous-quotes/'
        q_parser = QuoteParser()
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        with urlopen(req) as f:
            page = list(line.decode("utf-8").strip() for line in f.readlines())

        for eachline in page:
            q_parser.feed(eachline)

        return q_parser.quotes

    def _get_random_quote(self):
        num = random.randint(0, len(self.quotes) - 1)
        return self.quotes[num]

    def randomize_key(self):
        alphabet = self.ALPHABET.copy()
        random.shuffle(alphabet)
        return alphabet

    def _encode_quote(self):
        return "".join([self.key[ord(char) - 65] if char.isalpha() else char for char in self.quote.quote])

    def _get_empty_guessed(self):
        return {letter: ' ' for letter in self.key}

    def guess_letter(self, change_val=None, enter_val=None):
        self._change_letter(change_val.upper(), enter_val.upper())
        return self.WIN if self.is_win() else self.STILL_PLAYING

    @staticmethod
    def check_letter(change_val=None, enter_val=None):
        if not change_val or not enter_val:
            raise ValueError
        elif not change_val.isalpha() or not enter_val.isalpha():
            raise ValueError

    def _change_letter(self, change_val, enter_val):
        self.guessed[change_val] = enter_val
        self.user_cryptogram = [self.guessed[letter] if letter.isalpha() else letter for letter in self.encoded_quote]

    def is_win(self):
        return "".join(self.user_cryptogram) == self.quote.quote


class QuoteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.quotes = list()
        self.curr_quote = None
        self.is_quote = False
        self.is_author = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'wp_quotepage_quote':
            self.is_quote = True
        elif tag == 'div' and attrs[0][0] == 'class'and attrs[0][1] == 'wp_quotepage_author':
            self.is_author = True

    def handle_endtag(self, tag):
        if self.is_quote:
            self.is_quote = False
        elif self.is_author:
            self.is_author = False

    def handle_data(self, data):
        if self.is_quote:
            match = re.match('^[0-9]*[.] ', data)
            if match:
                self.curr_quote = Quote(data[match.end(0):].upper())
        elif self.is_author and self.curr_quote.quote:
            self.curr_quote.author = data
            self.quotes.append(self.curr_quote)


class Quote:
    def __init__(self, quote):
        self.quote = quote
        self.author = None



