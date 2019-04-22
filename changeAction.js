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