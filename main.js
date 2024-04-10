import './style.css'
// import "redditData.json"

let values;

function fetchJSONData() {
    fetch("redditData.json")
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
    for (let i = 0; i < data.data.children.length; i++) {
        console.log(data.data.children[i].data.display_name);
    }
}


