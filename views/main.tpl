<html>
<head>
    <link href='main.css' rel='stylesheet' type='text/css'>
    <title>{{title or 'Cryptogram'}}</title>
</head>
<body>
<header>
    <h3>Welcome to</h3>
    <h1>CRYPTOGRAM</h1>
</header>

<main>
    <div ID="crypto">
        % for ind in game:
        <div class="el">
            % if (game[ind][1] != ' ' and game[ind][0] != ' '):
            <div class="guessedLetter letter">{{game[ind][0]}}</div>
            <div class="encodedLetter letter">{{game[ind][1]}}</div>
            % elif game[ind][0] == ' ' and game[ind][1] == ' ':
            <div class="letter">&nbsp;&nbsp;&nbsp;</div>
            <div class="encodedLetter letter">&nbsp;&nbsp;&nbsp;</div>
            % elif not game[ind][1].isalpha() and not game[ind][1].isspace():
                <div class="guessedLetter">{{game[ind][1]}}</div>
                <div class="encodedLetter letter">{{game[ind][1]}}</div>
            % else:
            <div class="guessedLetter">_</div>
            <div class="encodedLetter letter">{{game[ind][1]}}</div>
            % end
        </div>
        % end
    </div>
    <div id="forms">
        <form action="/" method="POST" ID="cryptoForm" name="cryptoForm">

            <label title="Always enter the 'encoded' letter for this field">Changing: </label>
            <input type='text' name='change_val' id='change_val'
                   title="Always enter the 'encoded' letter for this field" maxlength="1" autofocus/>
            <label title="The letter you wish to take the place of the 'encoded' letter">Entering: </label>
            <input type='text' name='enter_val' id='enter_val'
                   title="The letter you wish to take the place of the 'encoded' letter" maxlength="1"/>

            <br/>
            <input type='submit' name='sub' id='sub' class="primAction" value='Enter Letter'/>
            <a href='/new_game' id="new" class="secAction">New Game</a>
        </form>
    </div>
</main>

<footer>
    <p>Copyright &copy; 2019, Marissa Cleroux</p>
</footer>

<script>
    addEventListener('load', () => {
        let form = document.getElementById('cryptoForm');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            let changeVal = document.getElementById('change_val');
            let enterVal = document.getElementById('enter_val');
            console.log('change', changeVal, changeVal.value);
            console.log('enter', enterVal, enterVal.value);
            e.target.action = `/game/${changeVal.value}/${enterVal.value}`;
            form.submit();

        })
    });
</script>
</body>
</html>