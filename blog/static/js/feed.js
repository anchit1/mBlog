// need to make the bottom bar of the new post form
// visible upon focus

// language=JQuery-CSS

var header_profile_pic = $('#header-profile-pic');
header_profile_pic.click(function () {
    var dropdown = $('.dropdown');
    dropdown.removeClass('inactive')
    dropdown.addClass('active');
});