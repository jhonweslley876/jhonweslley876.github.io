let botão = document.getElementById('btn')
let nomeInput = document.getElementById('nome')
let valorInput = document.getElementById('valor')
let area = document.getElementById('area')
let estoqueInput = document.getElementById('estoque')
let save = JSON.parse(localStorage.getItem('save')) || [];
let pesquisaInput = document.getElementById('pesquisa')
let menu = document.getElementById('menu')
let areaMenu = document.getElementById('menu-area')
let menuF = false

pesquisaInput.addEventListener('input', function(){
    renderizar();
})

function renderizar() {
    area.innerHTML = '';


    let textoBusca = pesquisaInput.value.toLowerCase();

    save.forEach((item, index) => {

        if (!item.produto.toLowerCase().includes(textoBusca)) {
            return;
        }

        let caixa = document.createElement('div');
        caixa.classList.add('caixa');

        let nomeDiv = document.createElement('div');
        nomeDiv.classList.add('divDados')
        let nome = document.createElement('h2')
        nome.textContent = item.produto;

        let valorDiv = document.createElement('div');
        valorDiv.classList.add('divDados')
        let valor = document.createElement('h2')
        valor.textContent = 'R$' + item.valor;

        let removerDiv = document.createElement('div');
        removerDiv.classList.add('divDados')
        let remover = document.createElement('button')
        remover.textContent = 'remover';

        remover.addEventListener('click', function () {
            save.splice(index, 1);
            localStorage.setItem('save', JSON.stringify(save))
            renderizar();
        })

        let areaValores = document.createElement('div');
        areaValores.classList.add('divDados')
        let caixaValores = document.createElement('div')
        caixaValores.classList.add('caixaValores')

        let adicionarEstoque = document.createElement('button')
        adicionarEstoque.textContent = '+'
        adicionarEstoque.classList.add('botões')

        let estoque = document.createElement('p');
        estoque.textContent = item.estoque;

        let removerEstoque = document.createElement('button')
        removerEstoque.classList.add('botões')
        removerEstoque.textContent = '-'

        adicionarEstoque.addEventListener('click', function () {
            item.estoque++;
            renderizar()
            localStorage.setItem('save', JSON.stringify(save))
        })

        removerEstoque.addEventListener('click', function () {
            if (item.estoque > 0) {
                item.estoque--;
                renderizar()
                localStorage.setItem('save', JSON.stringify(save))
            } else {
                alert('O estoque já está vazio!');
            }
        })

        caixaValores.appendChild(adicionarEstoque)
        caixaValores.appendChild(estoque)
        caixaValores.appendChild(removerEstoque)

        areaValores.appendChild(caixaValores)
        nomeDiv.appendChild(nome)
        valorDiv.appendChild(valor)
        removerDiv.appendChild(remover)
        caixa.appendChild(nomeDiv)
        caixa.appendChild(valorDiv)
        caixa.appendChild(removerDiv)
        caixa.appendChild(areaValores)
        area.appendChild(caixa)

    })
}

menu.addEventListener('click', function(){
    menuF = !menuF

    if (menuF){
        
        let menuCaixa = document.createElement('div');
        menuCaixa.classList.add('menuCaixa')
        
        let inputNome = document.createElement('input')
        inputNome.textContent = 'aaaaa'
    
        menuCaixa.appendChild(inputNome)
        areaMenu.appendChild(menuCaixa)
    } else {
        document.body.style.background = 'black'
        areaMenu.remove();
    }
})

renderizar();

botão.addEventListener('click', function () {
    if (nomeInput.value != "" && !isNaN(valorInput.value) && !isNaN(estoqueInput.value)) {
        save.push({ produto: nomeInput.value, valor: Number(valorInput.value), estoque: Number(estoqueInput.value) });
        localStorage.setItem('save', JSON.stringify(save));
        renderizar();
        nomeInput.value = ''
        valorInput.value = ''
        estoqueInput.value = ''
    } else {
        alert('Valores inválidos!');
    }
})