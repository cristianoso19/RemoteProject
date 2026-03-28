console.log("API CATS");
const URL = "https://api.thecatapi.com/v1/images/search"

async function getNewCat() {
    const response = await fetch(URL);
    const data = await response.json();
    const img = document.querySelector('img');
    img.src = data[0].url;
} 
document.onload = getNewCat();