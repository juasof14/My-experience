document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('tareaInput');
  const boton = document.getElementById('agregarBtn');
  const lista = document.getElementById('listaTareas');

  const mensaje = document.createElement('div');
  mensaje.id = 'mensaje';
  mensaje.style.position = 'fixed';
  mensaje.style.bottom = '30px';
  mensaje.style.left = '50%';
  mensaje.style.transform = 'translateX(-50%)';
  mensaje.style.padding = '12px 24px';
  mensaje.style.borderRadius = '12px';
  mensaje.style.fontWeight = '600';
  mensaje.style.fontFamily = 'Arial, sans-serif';
  mensaje.style.color = '#fff';
  mensaje.style.boxShadow = '0 4px 15px rgba(0, 0, 0, 0.3)';
  mensaje.style.opacity = '0';
  mensaje.style.transition = 'all 0.6s ease';
  mensaje.style.pointerEvents = 'none';
  document.body.appendChild(mensaje);

  function mostrarMensaje(texto, tipo = 'info') {
    mensaje.textContent = texto;

    if (tipo === 'ok') {
      mensaje.style.background = 'linear-gradient(135deg, #00c853, #009624)';
    } else if (tipo === 'error') {
      mensaje.style.background = 'linear-gradient(135deg, #ff1744, #d50000)';
    } else {
      mensaje.style.background = 'linear-gradient(135deg, #333, #111)';
    }

    mensaje.style.transform = 'translateX(-50%) translateY(0)';
    mensaje.style.opacity = '1';

    setTimeout(() => {
      mensaje.style.opacity = '0';
      mensaje.style.transform = 'translateX(-50%) translateY(20px)';
    }, 2000);
  }

  let tareas = JSON.parse(localStorage.getItem('tareas')) || [];
  tareas.forEach(t => agregarTarea(t.texto, t.completada));

  function agregarTarea(texto, completada = false) {
    const li = document.createElement('li');
    li.textContent = texto;
    if (completada) li.classList.add('completed');
    li.addEventListener('click', () => {
      li.classList.toggle('completed');
      guardarTareas();
    });
    li.addEventListener('dblclick', () => {
      li.remove();
      guardarTareas();
      mostrarMensaje('Tarea eliminada ❌', 'error');
    });
    lista.appendChild(li);
    guardarTareas();
    mostrarMensaje('Tarea añadida ✅', 'ok');
  }

  function guardarTareas() {
    const tareas = [];
    lista.querySelectorAll('li').forEach(li => {
      tareas.push({
        texto: li.textContent,
        completada: li.classList.contains('completed')
      });
    });
    localStorage.setItem('tareas', JSON.stringify(tareas));
  }

  boton.addEventListener('click', () => {
    const texto = input.value.trim();
    if (texto !== '') {
      agregarTarea(texto);
      input.value = '';
      input.focus();
    }
  });

  input.addEventListener('keydown', e => {
    if (e.key === 'Enter') {
      const texto = input.value.trim();
      if (texto !== '') {
        agregarTarea(texto);
        input.value = '';
      }
    }
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Backspace' && input.value === '') {
      const ultimo = lista.lastElementChild;
      if (ultimo) {
        ultimo.remove();
        guardarTareas();
        mostrarMensaje('Última tarea eliminada ⌫', 'error');
      }
    }
  });
});

// 🌙 Botón para alternar modo oscuro
const btnModo = document.getElementById('modoBtn');

btnModo.addEventListener('click', () => {
  document.body.classList.toggle('dark');
  btnModo.textContent = document.body.classList.contains('dark')
    ? '☀️ Modo Claro'
    : '🌙 Modo Oscuro';
});
