let button = document.getElementById('imagem');
let dinheiroTela = document.getElementById('money');
let clique = document.getElementById('quant-clique')
let area = document.getElementById('area-melhorias')
let totalTela = document.getElementById('quant-total')
let areaUpgrades = document.getElementById('upgrades')
let quantClique = document.getElementById('cliques-totais')
let excluirDados = document.getElementById('excluir')
let areaDetalhesUpgrades = document.getElementById('caixa-informações-upgrades')

let dadosJogador = JSON.parse(localStorage.getItem('dadosJogador')) || {
    dinheiro: 0,
    totalDinheiro: 0,
    ganho: 1,
    ganhoPorSegundo: 0,
    quantClick: 0
}

let melhoria = JSON.parse(localStorage.getItem('melhoria')) || [
    {
        nome: 'cursor',
        preco: 15,
        quantidade: 0,
        ganho: 0.1,
        desbloqueio: 15,
        ganhoTotal: 0
    },

    {
        nome: 'vovó',
        preco: 100,
        quantidade: 0,
        ganho: 1,
        desbloqueio: 100,
        ganhoTotal: 0
    },
    {
        nome: 'fazenda',
        preco: 1000,
        quantidade: 0,
        ganho: 5,
        desbloqueio: 1250,
        ganhoTotal: 0
    },

    {
        nome: 'mina de cookies',
        preco: 12500,
        quantidade: 0,
        ganho: 10,
        desbloqueio: 12000,
        ganhoTotal: 0
    }
]

let upgrades = JSON.parse(localStorage.getItem('upgrades')) || [
    {
        nome: 'cliques em dobro',
        descrição: 'Aumente a produção de cps dos cursores pelo dobro.',
        valor: 100,
        desbloqueio: 10,
        efeito: 2,
        imagem: 'imagens/carro.png',
        aparece: true,
        caixa: false
    },
    {
        nome: 'festa das vovós',
        descrição: 'As vovós estão assando cookies em dobro',
        valor: 250,
        desbloqueio: 10,
        efeito: 2,
        imagem: 'imagens/carro.png',
        aparece: true,
        caixa: false // adicionando para não esquecer quando chegar em casa. caixa de informações do item. 
    },
    {
        nome: 'fazenda em dobro',
        descrição: 'Suas colheitas estão produzindo o dobro de frutas',
        valor: 500,
        desbloqueio: 10,
        efeito: 2,
        imagem: 'imagens/carro.png',
        aparece: true,
        caixa: false // adicionando para não esquecer quando chegar em casa. caixa de informações do item. 
    },
    {
        nome: 'cookies dourados',
        descrição: 'Suas minas de cookies encontraram cookies que valem o dobro!',
        valor: 250,
        desbloqueio: 10,
        efeito: 2,
        imagem: 'imagens/carro.png',
        aparece: true,
        caixa: false // adicionando para não esquecer quando chegar em casa. caixa de informações do item. 
    },
]

function comprar_upgrades(index){
    let compra = upgrades[index]
    let mel = melhoria[index]
    if (dadosJogador.dinheiro >= compra.valor){
        compra.aparece = false;
        criar_upgrades()
        adicionar_upgrades(index, false)
        salvar()
        dadosJogador.ganhoPorSegundo -= mel.ganhoTotal
        dadosJogador.dinheiro -= compra.valor;
        mel.ganho = mel.ganho * compra.efeito
        mel.ganhoTotal = mel.ganhoTotal * compra.efeito
        dadosJogador.ganhoPorSegundo += mel.ganhoTotal
        atualizarUpgrades()
    }
}

function criar_upgrades(){
    areaUpgrades.innerHTML = ''
    upgrades.forEach((item, index) =>{
        if (melhoria[index].quantidade >= item.desbloqueio && item.aparece){
            let upgr = document.createElement('div')
            upgr.classList.add('div-upgr')
            upgr.id = `upgr-${index}`

            let imagemUpgrade = document.createElement('img')
            imagemUpgrade.src = item.imagem
            imagemUpgrade.id = `imagem-upgrade-${index}`

            upgr.appendChild(imagemUpgrade)
            areaUpgrades.appendChild(upgr)

            imagemUpgrade.addEventListener('mouseenter', function(){
                adicionar_upgrades(index, true)
            })

            imagemUpgrade.addEventListener('mouseleave', function(){
                adicionar_upgrades(index, false)
            })

            imagemUpgrade.addEventListener('click', function(){
                comprar_upgrades(index);
            })
        }
    })
}

function adicionar_upgrades(index, tipo){
    if (tipo){
        areaDetalhesUpgrades.innerHTML = ''
        let up = upgrades[index]
        let AreaDosUpgrades = document.createElement('div');
        AreaDosUpgrades.classList.add('area-upgrades')
    
        let divisãoUpgrade = document.createElement('div')
        divisãoUpgrade.classList.add('divisão-upgrades')
    
        let nomeUpgrade = document.createElement('h3')
        nomeUpgrade.classList.add('Nome-upgrade')
        nomeUpgrade.textContent = up.nome
    
        let valorUpgrade = document.createElement('h3')
        valorUpgrade.classList.add('valor-upgrade')
        valorUpgrade.textContent = up.valor
        
        let descriçãoUpgrade = document.createElement('p')
        descriçãoUpgrade.classList.add('descrição-upgrade')
        descriçãoUpgrade.textContent = up.descrição
        
        divisãoUpgrade.appendChild(nomeUpgrade)
        divisãoUpgrade.appendChild(valorUpgrade)
        AreaDosUpgrades.appendChild(divisãoUpgrade)
        AreaDosUpgrades.appendChild(descriçãoUpgrade)
        areaDetalhesUpgrades.appendChild(AreaDosUpgrades)
    } else {
        areaDetalhesUpgrades.innerHTML = ''
    }
}

function compra(indice){

    let melhorias = melhoria[indice]

    if (Number(dadosJogador.dinheiro.toFixed(2)) >= melhorias.preco ){
        
        dadosJogador.dinheiro += 0.0000000000001
        
        dadosJogador.dinheiro -= melhorias.preco

        melhorias.preco = Number(
            (melhorias.preco * 1.2).toFixed(0)
        )
        
        melhorias.quantidade++
        
        dadosJogador.ganhoPorSegundo += melhorias.ganho;
        melhorias.ganhoTotal += melhorias.ganho

        criar_upgrades()
        renderizar()
        salvar()
    }
}

function adicionar(dinheiroTotal){
    
    area.innerHTML = ''
    melhoria.forEach((item, index) =>{
        if (Number(dinheiroTotal) >= item.desbloqueio && !document.getElementById(`melhoria-${index}`)){
            
            let caixa = document.createElement('div');
            caixa.classList.add('melhorias')
            caixa.id = `melhoria-${index}`
            
            let divisão = document.createElement('div')
            divisão.classList.add('divisão-compras-dados')

            let nome = document.createElement('h2')
            nome.textContent = item.nome;
            nome.classList.add('nome')
            divisão.appendChild(nome);
            
            let dadosMelhoria = document.createElement('div');
            dadosMelhoria.classList.add('dadosMelhoria')

            let valor = document.createElement('h3');
            valor.textContent = 'R$' + item.preco.toFixed(0);
            valor.id = `valor-${index}`
            valor.classList.add('valor')
            dadosMelhoria.appendChild(valor)

            let ganho = document.createElement('h3')
            ganho.id = `ganho-${index}`
            ganho.textContent = "+" + item.ganho
            dadosMelhoria.appendChild(ganho)

            
            let quantidadeDiv = document.createElement('div')
            quantidadeDiv.classList.add('quantidade')

            let quantidade = document.createElement('h3')
            quantidade.textContent = item.quantidade
            quantidade.id = `quant-${index}`
            quantidadeDiv.appendChild(quantidade)

            divisão.appendChild(dadosMelhoria)
            caixa.appendChild(divisão)
            caixa.appendChild(quantidadeDiv)
            area.appendChild(caixa)

            caixa.addEventListener('click', function(){
                compra(index)
            })

        }

    })
}

function atualizarValores(){

    melhoria.forEach((item, index) => {

        let valor =
        document.getElementById(`valor-${index}`);

        let quant =
        document.getElementById(`quant-${index}`);

        let ganho = document.getElementById(`ganho-${index}`)

        if(valor){
            valor.textContent =
            'R$' + item.preco.toFixed(0);
        }

        if(quant){
            quant.textContent =
            item.quantidade;
        }

        if (ganho){
            ganho.textContent = "+" + item.ganho
        }

    })

}

function atualizarUpgrades(){
     upgrades.forEach((item, index) =>{

        if (!item.aparece){
            clique.textContent = `Quantidade por segundo: ${dadosJogador.ganhoPorSegundo.toFixed(2)}`
        }
        

     })
}

function salvar() {
    localStorage.setItem('dadosJogador', JSON.stringify(dadosJogador));
    localStorage.setItem('melhoria', JSON.stringify(melhoria))
    localStorage.setItem('upgrades', JSON.stringify(upgrades))
}

function renderizar() {
    dinheiroTela.textContent =
        `dinheiro atual: ${dadosJogador.dinheiro.toFixed(0)}`
    clique.textContent =
        `Quantidade por segundo: ${dadosJogador.ganhoPorSegundo.toFixed(2)}`
    quantClique.textContent =
        `Quantidade de cliques no total: ${dadosJogador.quantClick}`
    totalTela.textContent = 
    `Quantidade total: ${dadosJogador.totalDinheiro.toFixed(0)}`
    
}

setInterval(function(){

    let ganho = dadosJogador.ganhoPorSegundo / 20;

    dadosJogador.dinheiro = Number(
        (dadosJogador.dinheiro + ganho)
    );

    dadosJogador.totalDinheiro = Number(
        (dadosJogador.totalDinheiro + ganho)
    );

    renderizar();
    atualizarValores()
    atualizarUpgrades()
    salvar();

}, 50)

button.addEventListener('click', function () {
    dadosJogador.quantClick++
    dadosJogador.dinheiro += dadosJogador.ganho
    dadosJogador.totalDinheiro += dadosJogador.ganho
    adicionar(dadosJogador.totalDinheiro)
    criar_upgrades()
    renderizar()
    salvar();
    
})

excluirDados.addEventListener('click', function(){
    localStorage.clear();
})

criar_upgrades()
adicionar(dadosJogador.totalDinheiro)
renderizar();
localStorage.clear()