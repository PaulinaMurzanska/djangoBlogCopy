$('.show_more').on('click', (event) => {
    $('.all').addClass('open');
    $('.more').addClass("hidden");
    $('.less').addClass("shown");

});

$('.show_less').on('click', (event) => {
    $('.all').removeClass('open');
    $('.less').removeClass('shown');
    $('.more').removeClass('hidden');


});

$('.hamburger-btn').on('click', (event) => {
    $('.menu-hidden').addClass('open');
    $(".hamburger-btn").addClass("hide");
    $(".close-btn").addClass("open");

});

$(".close-btn").on('click', (event) => {
    $('.menu-hidden').removeClass('open');
    $(".hamburger-btn").removeClass("hide");
    $(".close-btn").removeClass("open");

});