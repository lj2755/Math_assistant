function enviarSolicitud() {
    const operacion = document.getElementById("operacion").value;
    const expresion = document.getElementById("expresion").value;
    const variable = document.getElementById("variable").value;
  
    fetch("/calcular", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        operacion: operacion,
        expresion: expresion,
        variable: variable,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("resultado").innerText = data.resultado;
      })
      .catch((error) => {
        document.getElementById("resultado").innerText =
          "Ocurrió un error: " + error;
      });
  }
  