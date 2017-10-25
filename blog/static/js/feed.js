$('#new-post-input').focus(function () {
    $('#new-post-bottom').removeClass('inactive');
    $('#new-post-bottom').addClass('active');
});

$('#new-post-input').blur(function () {
    $('#new-post-bottom').removeClass('active');
    $('#new-post-bottom').addClass('inactive');
});