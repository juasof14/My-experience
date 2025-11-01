const input = document.getElementById('tareaInput');
const boton = document.getElementById('agregarBtn');
const lista = document.getElementById('listaTareas');

// Agregar tarea
boton.addEventListener('click', () => {
    const texto = input.value.trim();
    if (texto !== '') {
        const li = document.createElement('li');
        li.textContent = texto;
        li.addEventListener('click', () => li.classList.toggle('completed'));
        li.addEventListener('dblclick', () => li.remove());
        lista.appendChild(li);
        input.value = '';
    }
});