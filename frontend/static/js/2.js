buildList()

function buildList(){
    var serializedData = $("#createTaskForm").serialize();

        $.ajax({
            url: "flight_time/",
            type: 'POST',
            data: serializedData,
            success: function(response){
                $("#taskList").html('</br><i class="fa fa-paper-plane fa-2x fa-spin" aria-hidden="true"></i></br><h3></br> ' + response.flight + ' </h3></br><img src="' +response.url+ '" alt="Select your drone to display image!" style="width:500px;" />');
            },
            failure: function(data) {
                alert('Got an error dude');
            }
        })
        //$("#createTaskForm")[0].reset();
    };