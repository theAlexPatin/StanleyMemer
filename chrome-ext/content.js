// Pick out a random image from our collection.
function getImage() {
    return "https://img.ifcdn.com/images/eb5e7bd199a4392be162a2974778c47cccec9be2ba78091aa367068c992a8717_3.jpg";//chrome.extension.getURL("TooDank.jpg");
}

// Get all the images on a page.
var images = document.getElementsByTagName("img");

// Replace each image with a random one.
for (var i = 0; i < images.length; i++) {
    var image = images[i];
    image.src = getImage();
    var rand = Math.floor(Math.random() * 2) + 1
    if(rand == 1){
        image.src = getImage();
    }/*
    //image.src = getImage();
    var xhr = new XMLHttpRequest();
    var url = "http://localhost:5000/api/check_image";
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4 && xhr.status == 200){
            var json = JSON.parse(xhr.responseText);
            console.log(image);
            if(json['type'] == 'meme'){
                image.src = getImage();
            }
        }
    }
    var data = JSON.stringify({'url':image.src});
    xhr.send(data);*/
}