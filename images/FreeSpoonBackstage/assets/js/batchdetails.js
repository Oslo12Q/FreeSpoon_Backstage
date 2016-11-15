$(document).ready(function () {
	(function ($) {
		$.getUrlParam = function (name) {
			var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
			var r = window.location.search.substr(1).match(reg);
			if (r != null) return unescape(r[2]); return null;
		}
	})(jQuery);
	
	var id=$.getUrlParam('id');
	

	var DataTable=function(){
			
			

			

            $('#query').click(function(table){
				table_api.ajax.reload(null, false );
				console.log($('#name').val());
            });
            $('#clear').click(function(){
				$('#form_table')[0].reset();
				table_api.ajax.reload(null, true );
            });

			//表格渲染配置
            var table_api=$('#example').DataTable({
				dom: 'Bfrtip',
				buttons: [
				    {extend:'copy',text:'复制'},
					{extend:'csv',text:'导出csv格式'},
					{extend:'excel',text:'导出excel'},
					{
						extend:'print',
						text:'打印',
						message:'一家一农订单详情',
						customize:function(win){
							$(win.document.body)
								.css('font-size','10pt')
								/*.prepend(
									'<img src="http://datatables.net/media/images/logo-fade.png" style="position:absolute; top:0; left:0;" />'
								);*/
							$(win.document.body).find( 'table' )
								.addClass( 'compact' )
								.css( 'font-size', 'inherit' );
						}
						
					}
					
					
				],
                "processing": true,
                "serverSide": true,
                "paging":true,
                "iDisplayLength": 25,
				"sLoadingRecords": "加载中...",
                "order":[],
                "ajaxSource":"http://192.168.102.167:8080/order/",
				"fnServerParams":function(aoData){
					aoData.push(
						{'name':'filter[order_number]','value':$('#name').val()},
						{'name':'filter[order_mob]','value':$('#mob').val()},
						{'name':'filter[pay_status]','value':$('#pay_status option:selected').val()},
						{'name':'filter[pay_method]','value':$('#pay_method option:selected').val()},
						{'name':'filter[start_day]','value':$('#start_day').val()},
						{'name':'filter[batch_id]','value':id},
						{'name':'filter[end_day]','value':$('#end_day').val()}
					)
				},
               "columns": [
                            { "mData ": "col0"},
                            { "mData ": "col1"},
                            { "mData ": "col2"},
                            { "mData ": "col3"},
                            { "mData ": "col4"},
                            { "mData ": "col5"},
                            { "mData ": "col6"},
                            { "mData ": "col7"},
                            { "mData ": "col8"},
							{ "mData ": "col9"},
							{ "mData ": "col10"},
							{ "mData ": "col11"},
							{ "mData ": "col12"},
							{ "mData ": "col13"},
							{ "mData ": "col14"}
                        ],
                /*"columnDefs": [ 
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
				],*/
                "oLanguage": {
                    "sLengthMenu": "每页显示 _MENU_ 条记录",
                    "sZeroRecords": "对不起，查询不到任何相关数据",
                    "sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
                    "sInfoEmtpy": "找不到相关数据",
                    "sInfoFiltered": "(数据表中共为 _MAX_ 条记录)",
                    "sProcessing": "正在加载中...",
                    "sSearch": "搜索",
                    "oPaginate": {
                        "sFirst":    "第一页",
                        "sPrevious": " 上一页 ",
                        "sNext":     " 下一页 ",
                        "sLast":     " 最后一页 "
                    }
                },
				
            });			
    };
	
	var BatchList=function(){
		var api_table=$(batch).DataTable({
				"processing": true,
				"serverSide": true,
				"bLengthChange":false,
				"bFilter":false,
				"bPaginate":false,
				"bInfo":false,
                "ajaxSource":"http://192.168.102.167:8080/datasource/ajaxsource/api/",
				"columns": [
					{ "mData ": "col0"},
					{ "mData ": "col1"},
					{ "mData ": "col2"},
					{ "mData ": "col3"},
					{ "mData ": "col4"},
					{ "mData ": "col5"},
					{ "mData ": "col6"},
					{ "mData ": "col7"},
					{ "mData ": "col8"},
					{ "mData ": "col9"}
				],
				"fnServerParams":function(aoData){
					aoData.push(
						{'name':'filter[batch_name]','value':''},
						{'name':'filter[batch_mob]','value':''},
						{'name':'filter[batch_id]','value':id},
						{'name':'fileter[batch_status]','value':''}
					)
				},
				
		});
	};
	BatchList();
	DataTable();
});