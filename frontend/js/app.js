// Espera o HTML carregar completamente
document.addEventListener("DOMContentLoaded", function () {

    // Captura o formulário pelo ID
    const form = document.getElementById("form-gasto");

    // Escuta o evento de envio do formulário
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Impede recarregar a página

        // Captura os valores dos campos
        const valor = document.getElementById("valor").value;
        const categoria = document.getElementById("categoria").value;
        const data = document.getElementById("data").value;
        const descricao = document.getElementById("descricao").value;

        // Validação simples
        if (!valor || !categoria || !data || !descricao) {
            alert("Preencha todos os campos!");
            return;
        }

        // Cria um objeto gasto
        const gasto = {
            valor: parseFloat(valor),
            categoria: categoria,
            data: data,
            descricao: descricao
        };

        // Mostra no console (por enquanto)
        console.log("Gasto cadastrado:", gasto);

        // Limpa o formulário após salvar
        form.reset();

        alert("Gasto salvo com sucesso!");
    });

});
