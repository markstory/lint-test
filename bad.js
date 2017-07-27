if (/cakephp\.org/.test(document.domain)) {
  document.domain = 'cakephp.org';
}

App = {};
App.config = {
  url: 'https://search.cakephp.org/search',
  version: '3-0'
};

App.Book = (function() {
  function init() {
    // Show back to contents button.
    var backToTop = $('#back-to-contents');

    backToTop.bind('click', function(evt) {
      $('html,body').animate({scrollTop: 0}, 200);
      return false;
    });

    // Tooltips
    $("[data-toggle='tooltip']").tooltip();
  }

  return {
    init : init
  };
})();
