function getCreche(){
    return $("#creche").val()
}

function getCrecheTexto(){
    creche = $("#creche option:selected").text()
    creche = creche.substring(creche.indexOf('-') + 2, creche.indexOf('|')-1)

    return creche
}

function getModalidade(){
    return $("#modalidades").val()
}

function getModalidadeTexto(){
    modalidade = $("#modalidades option:selected").text()
    modalidade = modalidade.substring(0, modalidade.indexOf('-')-1)

    return modalidade
}

function listarModalidade(){
    idCreche = getCreche()

    $.ajax({
        url: "/modalidade/lista/" + idCreche,
        type:'GET',
        success: function (seletorMod) {
            $( "#modalidades" ).remove();
            $( seletorMod ).insertAfter( "#creche" );
            filtrarTabela(1, 4)
        },
    });
}