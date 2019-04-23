<html>
<head>
  <link href='css/main.css' rel='stylesheet' type='css'>
  <title>{{title or 'Cryptogram'}}</title>
</head>
<body>
    <header>
        <h1>You win!</h1>
    </header>

  <main>
      <form action="/game" method="POST" ID="play" name="play">
        <div style="display: flex; flex-wrap: wrap;">
            % for ind in game:
                <div class="el">
                    % if game[ind][1] != ' ' and game[ind][0] != ' ':
                        <div class="guessedLetter letter">{{game[ind][0]}}</div>
                        <div class="encodedLetter letter">{{game[ind][1]}}</div>
                    % elif game[ind][0] == ' ' and game[ind][1] == ' ':
                        <div class="guessedLetter letter">&nbsp;&nbsp;&nbsp;</div>
                        <div class="encodedLetter letter">&nbsp;&nbsp;&nbsp;</div>
                    % else:
                        <div class="guessedLetter letter">_</div>
                        <div class="encodedLetter letter">{{game[ind][1]}}</div>
                    % end
                </div>
                &nbsp;
            % end
        </div>
          <div>
          <br/>
            <input type='submit' name='play_again' id='play_again' value='Play Again!' />
        </div>
      </form>

  </main>

  <footer>
      <p>Copyright &copy; 2019, Marissa Cleroux</p>
  </footer>
</body>
</html>