(document).on('submit', 'form', function(form) {
  var $form = $(form);
  $.ajax({
    type: form.method,
    url: form.action,
    data: $form.serialize(),
    success: function(data) {
      $form.replace(data);
    }
  });
});