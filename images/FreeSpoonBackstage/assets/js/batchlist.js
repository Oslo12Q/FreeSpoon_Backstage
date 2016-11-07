$(document).ready(function () {
		
        var DataTable=function(){
            var dataParameter={};
            $('#query').click(function(){
                QueryParameter();
            });
            $('#clear').click(function(){
                ClearParameter();
            });

            function ClearParameter (){
                dataParameter={};
            };
            function QueryParameter (){
                dataParameter.name=$('#name').val();
                dataParameter.mob=$('#mob').val();
                dataParameter.status=$('option:selected').val(); 
                console.log(dataParameter);
            };

            $('#example').dataTable({
                "processing": true,
                "serverSide": true,
                "paging":true,
                "iDisplayLength": 10,
				"sLoadingRecords": "加载中...",
               
                "order":[],
                "ajaxSource":"http://192.168.44.128:8080/datasource/ajaxsource/api/",
				"fnServerParams":function(aoData){
					aoData.push(
						{'name':'batch_name','value':$('#name').val()}
					)
				},
                /*"ajax":{
                    "url":"data2.json",
                    "data":function(data){
                        $.each(dataParameter,function(key,value){
                            data[key]=value;
                        });
                    }
                },*/
               "columns": [
                            { "mData ": "col0"},
                            { "mData ": "col1"},
                            { "mData ": "col2"},
                            { "mData ": "col3"},
                            { "mData ": "col4"},
                            { "mData ": "col5"},
                            { "mData ": "col6"},
                            { "mData ": "col7"},
                            { "mData ": "col8"}
                        ],
                "columnDefs": [ 
                    {"targets": -1,"orderable": false},
                    {"targets": [0,1,2],"orderable": false},
					{"targets": [4,5],"searchable": false},
                    {"targets":-1,"mRender":function(data){
                        return "<a href='batchdetails.html?id="+data+"'>详情</a>"
                    }},
                    {'targets':3,'mRender':function(data){
                        if(data==1){
                            return '自提';
                        }else if(data==2){
                            return '送货上门';
                        }else{
                            return '自提/送货上门';
                        }
                    }},
                    {'targets':-3,'mRender':function(data){
                        if(data==0){
                            return '已开始';
                        }else if(data==-1){
                            return '已结束';
                        }else if(data==-2){
                            return '未开始';
                        }else if(data==1){
                            return '已截团';
                        }
                    }}
                ],
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
               /* "initComplete": function(settings, json) {
                    alert( 'DataTables has finished its initialisation.' );
                }
*/
            });
    };

DataTable();
});
