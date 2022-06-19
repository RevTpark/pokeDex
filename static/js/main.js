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

function showCameraSetup(){
    let element = document.getElementById('contentarea');
    if(element.style.display == 'none'){
        element.style.display = '';
        startup();
    }
    else{
        element.style.display = 'none';
        closeStream();
    }
}

var width = 350;
var streaming=false;

function startup() {
    video = document.getElementById('video');
    canvas = document.getElementById('canvas');
    startbutton = document.getElementById('startbutton');

    // access video stream from webcam
    navigator.mediaDevices.getUserMedia({
            video: true,
            audio: false
        })
        // on success, stream it in video tag
        .then(function(stream) {
            video.srcObject = stream;
            video.play();
        })
        .catch(function(err) {
            console.log("An error occurred: " + err);
        });
    
    
    video.addEventListener('canplay', function(ev) {
        if (!streaming) {
            height = video.videoHeight / (video.videoWidth / width);

            if (isNaN(height)) {
                height = width / (4 / 3);
            }

            video.setAttribute('width', width);
            video.setAttribute('height', height);
            canvas.setAttribute('width', width);
            canvas.setAttribute('height', height);
            streaming = true;
        }
    }, false);

    startbutton.addEventListener('click', function(ev) {
        takepicture();
        ev.preventDefault();
    }, false);

}

function takepicture() {
    var context = canvas.getContext('2d');
    if (width && height) {
        canvas.width = width;
        canvas.height = height;
        context.drawImage(video, 0, 0, width, height);

        var data = canvas.toDataURL('image/png');
        let file = dataURLtoFile(data, "new_image.png");
        let fileInput = document.getElementById('file');
        let container = new DataTransfer(); 
        container.items.add(file);
        fileInput.files = container.files;
    }
}

function closeStream(){
    let stream = document.getElementById('video').srcObject;
    stream.getTracks().forEach(function(track) {
        if (track.readyState == 'live' && track.kind === 'video') {
            track.stop();
        }
    });
}

function dataURLtoFile(dataurl, filename) {
    let arr = dataurl.split(','),
        mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]),
        n = bstr.length,
        u8arr = new Uint8Array(n);

    while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
    }

    return new File([u8arr], filename, { type: mime });
}