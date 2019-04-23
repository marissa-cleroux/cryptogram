<html>
<head>
  <link href='css/main.css' rel='stylesheet' type='text/css'>
  <title>{{title or 'Cryptogram'}}</title>
</head>
<body>
    <header>
        <h1>YOU WIN!</h1>
    </header>

  <main>
            <div ID="crypto">
            % for ind in game:
                <div class="el">
                    % if game[ind][1] != ' ' and game[ind][0] != ' ':
                        <div class="guessedLetter letter">{{game[ind][0]}}</div>
                        <div class="encodedLetter letter">{{game[ind][1]}}</div>
                    % elif game[ind][0] == ' ' and game[ind][1] == ' ':
                        <div class="letter">&nbsp;&nbsp;&nbsp;</div>
                        <div class="encodedLetter letter">&nbsp;&nbsp;&nbsp;</div>
                    % else:
                        <div class="guessedLetter">_</div>
                        <div class="encodedLetter letter">{{game[ind][1]}}</div>
                    % end
                </div>
                &nbsp;
            % end
        </div>
      <div id="forms">
      <form action="/" method="POST" ID="cryptoForm" name="cryptoForm">
            <a href='/new_game' id="new" >New Game</a>
      </form>
    </div>
  </main>
  <footer>
      <p>Copyright &copy; 2019, Marissa Cleroux</p>
  </footer>
</body>
</html>