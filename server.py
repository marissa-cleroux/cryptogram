from cryptogram import *
from bottle import route, run, template, static_file, redirect, error

game = Cryptogram()


@route('/')
def redirect_from_root():
    redirect('/game')


@route('/game')
def start():
    info = {'game': ~game, 'title': 'WELCOME'}
    return template('main.tpl', info)


@route('/new_game')
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
    return template('error.tpl', content='You must enter letters in both fields.')


@route('/game/', method="POST")
@route('/game//', method="POST")
@route('/game/<change_val>/', method="POST")
@route('/game//<enter_val>', method="POST")
@route('/game/<change_val>/<enter_val>', method="POST")
def guess(change_val=None, enter_val=None):
    game_return = game.guess_letter(change_val, enter_val)
    if game_return == 0:
        redirect('/game')
    elif game_return == 1:
        redirect('/win')
    else:
        redirect('/error')


@route('/<filename:re:.*\.css>')
def read_css(filename):
    return static_file('main.css', root='static/css')


@route('/<filename:re:.*\.ico>')
def read_ico(filename):
    return static_file('favicon.ico', root='./')


@route('/<filename:re:.*\.js>')
def read_js(filename):
    print('read')
    return static_file('changeAction.js', root='static/js')


run(host='localhost', port=9001, debug=True)
