$(document).ready(function() {
    $('.menu-burger__header').click(function() {
        $('.menu-burger__header').toggleClass('open-menu');
        $('.menu').toggleClass('open-menu');
    });
    $
});

$(document).on('click', function(event) {
    // Проверяем, является ли элемент, на который было нажато, ребенком элемента с классом 'my-class'.
    if (!$(event.target).closest('.open-menu').length) {
      // Удаляем класс 'active' у элемента с классом 'my-class'.
      $('.menu').removeClass('open-menu');
    }
  });

