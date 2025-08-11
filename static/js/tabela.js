function abrirDetalhe(idLista){
    $.ajax({
        url: '/lista/detalhe/' + idLista,
        type:'GET',
        success: function (detalhe) {
            $( "#modal-body" ).empty().append( detalhe );
        },
    });
}