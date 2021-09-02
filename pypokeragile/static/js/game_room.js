window.onload = function () {
           
    const socket = io('http://127.0.0.1:5000');

    socket.on('connect', () => {
        socket.send('User has connected!', {'room': room_key})
    })

    // document.querySelector("form").addEventListener("submit", function(event){
    //     event.preventDefault()
    //     console.log('sendMessage')
    //     socket.emit('sendMessage', {msg: event.target[0].value})
    // })

    // socket.on('getMessage' ,(msg) => {
    //     console.log(msg)
    //     const list = document.querySelector("#messages");
    //     list.append('<li>'+msg.msg+'</li>')
    // })
}


// $(document).ready(function() {

// 	var socket = io.connect('http://127.0.0.1:5000');

// 	socket.on('connect', function() {
// 		socket.send('User has connected!');
// 	});

// 	socket.on('message', function(msg) {
// 		$("#messages").append('<li>'+msg+'</li>');
// 		console.log('Received message');
// 	});

// 	$('#sendbutton').on('click', function() {
// 		socket.send($('#myMessage').val());
// 		$('#myMessage').val('');
// 	});

// });