'use strict';
const $ = window.$;

$(function () {
  $("input[type='password'][data-eye]").each(function (i) {
    const $this = $(this);
    const id = 'eye-password-' + i;

    $this.wrap($('<div/>', {
      style: 'position:relative',
      id: id
    }));

    $this.css({
      paddingRight: 60
    });
    $this.after($('<div/>', {
      html: 'Show',
      class: 'btn btn-primary btn-sm',
      id: 'passeye-toggle-' + i
    }).css({
      position: 'absolute',
      right: 10,
      top: ($this.outerHeight() / 2) - 12,
      padding: '2px 7px',
      fontSize: 12,
      cursor: 'pointer'
    }));

    $this.after($('<input/>', {
      type: 'hidden',
      id: 'passeye-' + i
    }));

    const invalidFeadback = $this.parent().parent().find('.invalidFeedback');

    if (invalidFeadback.length) {
      $this.after(invalidFeadback.clone());
    }

    $this.on('keyup paste', function () {
      $('#passeye-' + i).val($(this).val());
    });
    $('#passeye-toggle-' + i).on('click', function () {
      if ($this.hasClass('show')) {
        $this.attr('type', 'password');
        $this.removeClass('show');
        $(this).removeClass('btn-outline-primary');
      } else {
        $this.attr('type', 'text');
        $this.val($('#passeye-' + i).val());
        $this.addClass('show');
        $(this).addClass('btn-outline-primary');
      }
    });
  });

  $('.my-login-validation').submit(function () {
    const form = $(this);
    if (form[0].checkValidity() === false) {
      const evt = event;
      evt.preventDefault();
      evt.stopPropagation();
    }
    form.addClass('was-validated');
  });
});
