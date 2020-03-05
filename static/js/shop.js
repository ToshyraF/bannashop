$(function(){
    
   

    // mainmodal
    $('#mainmodal').on('shown.bs.modal', function () {
        // $('#modal1').css("filter","blur(5px)");
        })
    $('#myModal').on('shown.bs.modal', function () {
        $('#mainmodal').css("filter","blur(5px)");
    })
    $('#myModal').on('hidden.bs.modal', function () {
        $('#mainmodal').css("filter","blur(0px)");
    })

        $('.collapsible').collapsible();
        $(".js-example-tags").select2();
})