var tab = null

$('.nav-item a').on('click', function (e) {
    e.preventDefault();
    $('.nav-item a, .active').removeClass('active');
    $(this).addClass('active');
});

function resetarFiltro(){
    $('.nav-item a, .active').removeClass('active');
    $('#filtro-inicial').addClass('active');
}

function filtrarTabela(status){
    $.ajax({
        url: "/lista/status/" + getCreche() + "/" + getModalidade() + "/" + status,
        type:'GET',
        success: function (listaVagas) {

            if ( tab != null){
                tab.destroy();                
            }

            $( "#lista" ).remove();
            $( "#div-lista" ).append( listaVagas );
            $( "#titulo-lista").append(getCrecheTexto() + " - " + getModalidadeTexto())

            tab = $("#lista").DataTable({
                "dom": "Bfrtip",
                'aoColumnDefs': [{
                    'bSortable': false,
                    'aTargets': ['nosort']
                }],
                "bPaginate": true,
                "bLengthChange": false,
                "bFilter": true,
                "bInfo": true,
                "pageLength": 25,
                "bAutoWidth": false,
                "language":{
                    "sEmptyTable": "Nenhum registro encontrado",
                    "sInfo": "Mostrando _END_ de _TOTAL_ registro(s)",
                    "sInfoEmpty": "Mostrando 0 até 0 de 0 registro(s)",
                    "sInfoFiltered": "(Filtrados de _MAX_ registros)",
                    "sLengthMenu": "_MENU_ resultados por página",
                    "sZeroRecords": "Nenhum registro encontrado",
                    search: "_INPUT_",
                    searchPlaceholder: "Pesquisar",
                    "oPaginate": {
                        "sNext": ">",
                        "sPrevious": "<",
                        "sFirst": "<<",
                        "sLast": ">>"
                    }
                }
            });
            

        },
    });
}