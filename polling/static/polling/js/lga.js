
alert("Working");
var selectElement = document.getElementById("mySelect");

selectElement.addEventListener('change', ()=>{
    sendSelectedValue();
})

function sendSelectedValue() {
    var selectedValue = selectElement.value;
  
    fetch("/polling/lga_total/", {
      method: "POST",
      body: JSON.stringify({ lga_id: selectedValue }),
      headers: {
        "Content-Type": "application/json"
      }
    })
    .then(response => response.json())
    .then(data => {
      // Handle the API response here
      alert(data);
      console.log(data);
    })
    .catch(error => {
      // Handle any errors
      console.error(error);
    });
  }



