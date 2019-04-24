<html>
<head>
    <link href='main.css' rel='stylesheet' type='text/css'>
    <title>{{title or 'Cryptogram'}}</title>
</head>
<body>
<header>
    <h3>cryptogram</h3>
    <h1>YOU WIN!</h1>
</header>

<main>
    <div ID="crypto">
        % for ind in game:
        <div class="el">
            % if game[ind][1] != ' ':
            <div class="guessedLetter letter">{{game[ind][0]}}</div>
            <div class="encodedLetter letter">{{game[ind][1]}}</div>
            % else:
            <div class="letter">&nbsp;&nbsp;&nbsp;</div>
            <div class="encodedLetter letter">&nbsp;&nbsp;&nbsp;</div>
            % end
        </div>
        % end
    </div>
    <div id="author">{{author}}</div>
    <div class="center">
        <a href='/new_game' id="new" class="primAction">New Game</a>
    </div>
</main>
<footer>
    <p>Copyright &copy; 2019, Marissa Cleroux</p>
</footer>
</body>
</html>