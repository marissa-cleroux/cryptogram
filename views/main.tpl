<html>
<head>
  <link href='./main.css' rel='stylesheet' type='css'>
  <title>{{title or 'Cryptogram'}}</title>
</head>
<body>
    <header>
        <h1>Cryptogram Game</h1>
    </header>

  <main>
      <form action="/game" method="POST" ID='cryptoForm'>
        <div style="display: flex; flex-wrap: wrap;">
            % for ind in game:
                <div class="el">
                    % if game[ind][1] != ' ':
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
            <div>
                <label>Changing: </label>
                <input type='text' name='change_val' id='changeVal' />
            </div>
            <br/>
            <div>
                <label>Entering: </label>
                <input type='text' name='enter_val' id='enterVal' />
            </div>
            <input type='submit' name='submit' id='submit' value='guess' />
        </div>
      </form>

  </main>

  <footer>
      <p>Copyright &copy; 2019, Marissa Cleroux</p>
  </footer>

    <script>
        addEventListener('load', ()=>{
            let form = document.getElementById('cryptoForm');
            form.addEventListener('submit', (e)=>{
                e.preventDefault();
                let changeVal = document.getElementById('changeVal');
                let enterVal = document.getElementById('enterVal');
                e.target.action = `/game/${changeVal.text}/${enterVal.text}`;
                e.submit();
        })
    });
    </script>
</body>
</html>