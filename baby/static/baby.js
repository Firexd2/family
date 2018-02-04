$(document).ready(function() {

    var volume = 0;
    var objects_all_volume = $('.all-volume');
    for (var i=0;i<objects_all_volume.length;i++) {
        volume += parseInt(objects_all_volume.eq(i).text())
    }
    $('#all-volume').text(volume);


    $('.volume').on('click', function () {
        if ($(this).find('.detail-eat').is(':hidden')) {
            $(this).find('.detail-eat').show()
        } else {
            $(this).find('.detail-eat').hide()
        }
    });

    $('.delete').on('click', function () {
         var id = $(this).children().attr('id');
         $.post('/baby/delete/', {'id': id});
        location.reload();
    });
});