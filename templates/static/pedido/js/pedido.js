function dados_carros() {
    const placa = document.getElementById('placa').value;
    console.log(placa);
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    const data = new FormData();
    data.append('placa', placa);

    fetch('/pedido/achar_carro/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data,
    })
    .then(function(result) {
        return result.json();
    })
    .then(function(data) {
        console.log(data.carro.cliente_id);

        document.getElementById('carro_form').style.display = 'block';
        document.getElementById('nome').value = data.carro.carro;
        document.getElementById('ano').value = data.carro.ano;
        document.getElementById('cliente').value = data.carro.cliente;
        document.getElementById('id_carro').value = data.carro.id;
        document.getElementById('id_cliente').value = data.carro.cliente_id;
        // Adicione outras atribuições de valores aos campos do formulário conforme necessário
    })
}