from cryptogram import *
from bottle import route, run, template, static_file, request

game = Cryptogram()

@route('/game')
def start():
    info = {'game': ~game, 'title': 'WELCOME'}
    print(~game)
    print(game.quote)
    return template('main.tpl', info)


@route('/game/<change_val>/<enter_val>', method="GET")
def guess(change_val, enter_val):
    game_return = game.guess_letter(change_val, enter_val)
    if game_return == 0:
        start()
    elif game_return == 1:
        pass #win!
    else:
        pass #error


@route('/<filename:re:.*\.css>')
def read_file(filename):
    print('read called')
    print(filename)
    return static_file(filename, root='./styles/')


run(host='localhost', port=9001, debug=True)
