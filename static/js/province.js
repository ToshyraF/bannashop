$(function(){
    $('table>tbody>tr').click(function(){
        window.location.href = "/shop"
    })
    $('.collapsible').collapsible();
    $(".js-example-tags").select2();
})