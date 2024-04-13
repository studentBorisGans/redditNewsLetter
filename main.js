import './style.css'
// import "redditData.json"

let values;
let baseUrl = "https://www.reddit.com/r/";
let search;
let newSearch;

document.getElementById("submitButton").onclick = function() {
    search = document.getElementById("subreddit").value
}
newSearch = search;

setInterval(function() {
    // console.log(search);  
    if (newSearch != search) {
        newSearch = search
        console.log(search)
    }

}, 1000)





// bruh i dont even need the api lmao
// nevermind I only need it for searching, but not for accessing posts
function loadJSON(path, success, error) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          success(JSON.parse(xhr.responseText));
        }
        else {
          error(xhr);
        }
      }
    };
    xhr.open('GET', path, true);
    xhr.send();
}



function fetchJSONData() {
    fetch("redditContent.json")
        .then((res) => {
            if (!res.ok) {
                throw new Error
                    (`HTTP error! Status: ${res.status}`);
            }
            return res.json();
        })
        .then((data) => 
                // values = JSON.parse(data))
                // console.log(data))
                showSubReds(data))
        .catch((error) => 
               console.error("Unable to fetch data:", error));
}
fetchJSONData();

function showSubReds(data) {
    console.log(data.data.children[0])
    console.log(baseUrl + data.data.children[0].data.display_name + ".json");
    loadJSON(baseUrl + data.data.children[0].data.display_name + ".json", jsonRequest);
    for (let i = 0; i < data.data.children.length; i++) {
        console.log(data.data.children[i].data.display_name);
    }
}

function jsonRequest(data) {
    console.log(data);

}

// document.getElementById("test").innerHTML = search;
