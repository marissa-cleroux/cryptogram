from cryptogram import *
from bottle import route, run, template, static_file, request

game = Cryptogram()


@route('/game')
def start():
    info = {'game': ~game, 'title': 'WELCOME'}
    print(game.quote)
    return template('main.tpl', info)


@route('/game/<change_val>/<enter_val>', method="POST")
def guess(change_val, enter_val):
    game_return = game.guess_letter(change_val, enter_val)
    if game_return == 0:
        info = {'game': ~game, 'title': 'WELCOME'}
        return template('main.tpl', info)
    elif game_return == 1:
        print('win')
    else:
        print('error')


@route('/<filename:re:.*\.css>')
def read_css(filename):
    print('read called')
    return static_file('main.css', root='./styles/')


@route('/<filename:re:.*\.ico>')
def read_ico(filename):
    print('read called')
    return static_file('favicon.ico', root='./')


run(host='localhost', port=9001, debug=True)
