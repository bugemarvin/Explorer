const $ = window.$;
$(document).ready(function(){
        $('[data-bg-img').each(function () {
          $(this).css({
            'background-image': `url(${$(this).data('bg-img')})`
          });
        })
})