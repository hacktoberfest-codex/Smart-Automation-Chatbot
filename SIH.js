$(document).ready(function () {
    $('#send-button').click(function () {
        sendMessage();
    });

    $('#user-input').keypress(function (e) {
        if (e.which === 13) {
            sendMessage();
        }
    });

    function sendMessage() {
        const userMessage = $('#user-input').val();
        $('#chat-box').append(`<p class="user-message">You: ${userMessage}</p>`);
        $('#user-input').val('');

        $.ajax({
            type: 'POST',
            url: '/api/chat',  // corresponds to backend route
            contentType: 'application/json',
            data: JSON.stringify({ message: userMessage }),
            success: function (response) {
                $('#chat-box').append(`<p class="bot-message">Bot: ${response.response}</p>`);
            },
        });
    }
});
