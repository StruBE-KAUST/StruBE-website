$(document).ready(function () {
    $(".submit_button").click(function(e) {
        var button = $(this);
        var form = $(this).parents('form:first')[0];
        if(form.checkValidity() == true) {
            var l = Ladda.create(this);
            l.start();
            form.submit();
        }
    });
});
