$(document).ready(function () {

    

    (function ($) {
        $.getUrlParam = function (name) {
            var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
            var r = window.location.search.substr(1).match(reg);
            if (r != null) return unescape(r[2]); return null;
        }
    })(jQuery);

    var id=$.getUrlParam('id');
    console.log(id);

    $('#example').dataTable({
        "bProcessing": true,
        "ajax":id+"data1.json",
        "columns": [
                    { "data": "id"},
                    { "data": "reseller_mob"},
                    { "data": "user_id"},
                    { "data": "user_name"},
                    { "data": "recipient_type"},
                    { "data": "total_fee"},
                    { "data": "order_status"},
                    { "data": "payment_method"},
                    { "data": "payment_id"},
                    { "data": "order_time"},
                    { "data": "payment_time"},
                    { "data": "commodity"},
                    { "data": "address"},
                    { "data": "des"},
                    { "data": "logistics_id"}
                ],
        "columnDefs": [ 
            {"targets": -1,"orderable": false},
            {"targets": [0,1,2,3],"orderable": false},
            {'targets':4,'mRender':function(data){
                if(data==1){
                    return '自提';
                }else if(data==2){
                    return '送货上门';
                }
            }},
            {'targets':6,'mRender':function(data){
                if(data==-2){
                    return '已取消';
                }else if(data==-1){
                    return '未付款';
                }else if(data==0){
                    return '已付款';
                }else if(data==1){
                    return '已退款';
                }
            }},
            {'targets':7,'mRender':function(data){
                if(data==1){
                    return '微信';
                }else if(data==2){
                    return '余额';
                }else if(data==3){
                    return '微信+余额';
                }
            }}
        ],
        'oLanguage': {
            "sLengthMenu": "显示_MENU_条 ",
            "sSearch": "搜索",
            "oPaginate": {
            "sPrevious": "前一页",
            "sNext": "后一页"
            },
        },

    });

});