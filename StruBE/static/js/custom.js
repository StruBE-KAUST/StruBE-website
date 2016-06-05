$(document).ready(function () {
    $(".submit_button").click(function(e) {
        var button = $(this);
        var l = Ladda.create(this);
        l.start();
        var form = $(this).parents('form:first');
        form.submit();
    });
});
