// need to make the bottom bar of the new post form
// visible upon focus

// language=JQuery-CSS
// var new_post_input = $('#id_post_content');
// var new_post_bottom = $('#new-post-bottom');
// new_post_input.focus(function () {
//     new_post_bottom.removeClass('inactive');
//     new_post_bottom.addClass('active');
// });
//
// new_post_input.blur(function () {
//     new_post_bottom.removeClass('active');
//     new_post_bottom.addClass('inactive');
// });

var header_profile_pic = $('#header-profile-pic');
header_profile_pic.click(function () {
    var dropdown = $('.dropdown');
    dropdown.removeClass('inactive')
    dropdown.addClass('active');
});