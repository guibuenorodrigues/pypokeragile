
window.onload = function () {

    const create_button = document.querySelector("#btn_create");
    create_button.addEventListener('click', handle_create_room);

}


function handle_create_room(e) {
    
    e.preventDefault();

    formElem = document.querySelector('#form_new_room');
    if(!formElem.reportValidity()){
        console.log('html5 validation form is returning FALSE');
        return false;
    }
    
    // get data from form to a json object    
    data = get_input_data()

    fetch("/api/v1/rooms/create", {
        method: "POST",
        redirect: "follow",
        headers: new Headers({
            'Content-Type': 'application/json',
            'x-content-type': 'view'
        }),
        body: JSON.stringify(data)
    })
        .then(function (response) {
            if(response.redirected){
                window.location = response.url
            }
        })
        .catch(function (err) {
            console.log(err)
        });


}

function get_input_data() {
   
    const room_name = document.querySelector("#room_name").value;
    const owner_name = document.querySelector("#owner_name").value;
    const owner_email = document.querySelector("#owner_email").value;
    const room_password = document.querySelector("#room_password").value;
    

    let formData = new FormData();
    formData.append('room_name', room_name);
    formData.append('owner_name', owner_name);
    formData.append('owner_email', owner_email);
    formData.append('room_password', room_password);

    let jsonObject = {};

    for (const [key, value] of formData) {
        jsonObject[key] = value;
    }

    return jsonObject
}

