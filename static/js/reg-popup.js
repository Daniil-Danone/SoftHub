const regPopup = document.getElementById('reg-popup');
const regBtn = document.getElementById('signin');
const regClose = document.getElementById('close');

function add_class() {
  regPopup.classList.add('popup__active');
}

function remove_class() {
  regPopup.classList.remove('popup__active');
}

regBtn.onclick = add_class;
regClose.onclick = remove_class;