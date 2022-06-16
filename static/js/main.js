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

function handleSearchTypeToggle(){
    let ele = document.getElementById('changeSerachType');
    if(ele.innerHTML == 'Name'){
        ele.innerHTML = 'Type';
        ele.classList.remove('search-btn-name');
        ele.classList.add('search-btn-type');
        document.getElementById('searchPokemon').style.display = 'none';
        document.getElementById('type1').style.display = '';
        document.getElementById('type2').style.display = '';
    }
    else{
        ele.innerHTML = 'Name';
        ele.classList.add('search-btn-name');
        ele.classList.remove('search-btn-type');
        document.getElementById('searchPokemon').style.display = '';
        document.getElementById('type1').style.display = 'none';
        document.getElementById('type2').style.display = 'none';
    }
}

function handleTypeSearch(){
    let type1 = document.getElementById('type1').value.toLowerCase();
    let type2 = document.getElementById('type2').value.toLowerCase();
    let list = document.getElementsByClassName('poke-card');
    for(let i=0;i<list.length;i++){
        let temp = list[i].getElementsByClassName('poke-type-container')[0];
        let temp_type1 = temp.getElementsByClassName(type1+'-type');
        if(type2 != "none"){
            let temp_type2 = temp.getElementsByClassName(type2+'-type');
            if(temp_type1.length != 0 && temp_type2.length != 0){
                list[i].style.display = '';
            }
            else{
                list[i].style.display = 'none';
            }
        }
        else if(temp_type1.length != 0){
            list[i].style.display = '';
        }
        else{
            list[i].style.display = 'none';
        }
    }
}