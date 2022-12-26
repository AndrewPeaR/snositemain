function ModalWindow() {
    // создаём модальное окно
    var modal = $modal();
    // при клике по кнопке #show-modal
    document.querySelector('#emailsubmit').addEventListener('click', function (e) {
        // отобразим модальное окно
        modal.show();
    });
}