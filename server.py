from cryptogram import *
from bottle import route, run, template, static_file, request

game = Cryptogram()

@route('/game')
def start():
    content = ''
    for index, letter in enumerate(game.encoded_quote):
        content += f'''<div class='letter'>
                                <span class='guessedLetter'>{game.user_cryptogram[index]}</span>
                                <span class='encodedLetter'>{letter}</span>
                            </div>'''

    info = {'content': content, 'title': 'WELCOME'}
    return template('main.tpl', info)


@route('/game/<change_val>/<enter_val>', method="POST")
def guess(change_val, enter_val):
    game_return = game.guess_letter(change_val, enter_val)
    if game_return == 0:
        start()
    elif game_return == 1:
        pass #win!
    else:
        pass #error


@route('/styles/<filename:path>')
def read_file(filename):
    return static_file(filename, root='./styles/')


run(host='localhost', port=9001, debug=True)
