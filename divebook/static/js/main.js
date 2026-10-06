document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('welcome-button');
    const message = document.getElementById('welcome-message');

    button.addEventListener('click', function () {
        message.textContent = 'Nuevas funciones proximamente...';
    });
});