function exibir_form(tipo){

    add_peca = document.getElementById('adicionar_peca')
    add_servico = document.getElementById('adicionar_servico')

    if(tipo == "1"){
        add_peca.style.display = "none"
        add_servico.style.display = "block"

    }else if(tipo == "2"){
        add_servico.style.display = "none";
        add_peca.style.display = "block"
    }

}