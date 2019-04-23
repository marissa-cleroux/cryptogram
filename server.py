from cryptogram import *
from bottle import route, run, template, static_file, redirect

game = Cryptogram()


@route('/')
def redirect_from_root():
    redirect('/game')


@route('/game')
def start():
    info = {'game': ~game, 'title': 'WELCOME'}
    print(game.quote)
    return template('main.tpl', info)


@route('/game', method='POST')
def new_game():
    game.start_new_game()
    redirect('/game')


@route('/win')
def win():
    info = {'game': ~game, 'title': 'WELCOME'}
    if game.is_win():
        return template('win.tpl', info)
    else:
        redirect('/game')


@route('/error')
def error():
    pass


@route('/game/<change_val>/<enter_val>', method="POST")
def guess(change_val, enter_val):
    game_return = game.guess_letter(change_val, enter_val)
    if game_return == 0:
        redirect('/game')
    elif game_return == 1:
        redirect('/win')
    else:
        redirect('/error')


@route('/css/<filename:re:.*\.css>')
def read_css(filename):
    print('read called')
    return static_file('main.css', root='static/css')


@route('/<filename:re:.*\.ico>')
def read_ico(filename):
    return static_file('favicon.ico', root='./')


run(host='localhost', port=9001, debug=True)
