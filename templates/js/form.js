$(document).ready(function(){

    $('form').on('submit', function(event){

        $.ajax({
            data : {
                name : $('#nameinput').val(),
                email : $('#emailinput').val()
            },
            type : 'POST',
            url : '/process'
        })
        .done(function(data) {

            if(data.error){
                $('#ErrorAlert').text(data.error).show();
                $('#SuccessAlert').hide();
            }
            else{
                $('#SuccessAlert').text(data.name).show();
                $('#ErrorAlert').hide();
            }
        });

        event.preventDefault();

    });

});