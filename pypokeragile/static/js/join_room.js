
window.onload = function () {

    const create_button = document.querySelector("#btn_join");
    create_button.addEventListener('click', handle_join_room);

}


function handle_join_room(e) {
    e.preventDefault()

    fetch("/api/v1/room", {
        method: "POST",
        redirect: "follow",
        headers: new Headers({
            'Content-Type': 'application/json',
            'x-content-type': 'view'
        }),
        body: JSON.stringify(get_input_data())
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
    const email = document.querySelector("#email").value;
    const room_password = document.querySelector("#room_password").value;

    let formData = new FormData();
    formData.append('room_name', room_name);
    formData.append('email', email);
    formData.append('room_password', room_password);

    let jsonObject = {};

    for (const [key, value] of formData) {
        jsonObject[key] = value;
    }

    return jsonObject
}

