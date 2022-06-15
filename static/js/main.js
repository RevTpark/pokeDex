function handleSearch(){
    let query = document.getElementById('searchPokemon').value.toLowerCase();
    let list = document.getElementsByClassName('poke-card');
    for(let i=0;i<list.length;i++){
        let val = list[i].getElementsByClassName('poke-name')[0].innerHTML.toLowerCase();
        if(val.indexOf(query) > -1){
            list[i].style.display = '';
        }
        else{
            list[i].style.display = 'none';
        }
    }
}