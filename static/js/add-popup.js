const addPopup = document.getElementById('add-popup');
const addBtn = document.getElementById('add');

function handleClick() {
  addPopup.classList.toggle('popup__active');
}

addBtn.onclick = handleClick;