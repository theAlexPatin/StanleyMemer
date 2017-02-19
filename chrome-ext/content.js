// Pick out a random image from our collection.
function getImage() {
    return "https://img.ifcdn.com/images/eb5e7bd199a4392be162a2974778c47cccec9be2ba78091aa367068c992a8717_3.jpg";//chrome.extension.getURL("TooDank.jpg");
}

// Get all the images on a page.
var images = document.getElementsByTagName("img");

// Replace each image with a random one.
for (var i = 0; i < images.length; i++) {
    var image = images[i];
    console.log(image)
    //image.src = getImage();
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/api/check_image";
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = processRequest;
    function processRequest(e){
        if(xhr.readyState == 4 && xhr.status == 200){
            var json = JSON.parse(xhr.responseText);
            console.log(json)
            if(json['type'] == 'meme'){
                console.log(json['type'])
                image.src = getImage();
            }
        }
    }
    var data = JSON.stringify({'url':image.src});
    xhr.send(data);
}