from cryptogram import *
from bottle import route, run, template, static_file, request


@route('/game')
def start():
    form = '''
    <form action="/" method="POST">
        <div>
    '''
    game = Cryptogram()
    for index, letter in enumerate(game.encoded_quote):
        form += template("<span>{{letter}}</span>", letter=letter)
    form += '''
            <br/>
            <div>
                <label>Changing: </label>
                <input type='text' name='changing'>
            </div>
            <br/>
            <div>
                <label>Entering: </label>
                <input type='text' name='entering'>
            </div>
        </div>
    </form>'''
    return form


@route('/game/<changing>/<entering>', method="POST")
def guess():
    pass

run(host='localhost', port=9001, debug=True)