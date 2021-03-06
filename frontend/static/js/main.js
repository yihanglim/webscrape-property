		/*
			KEY COMPONENTS:
			"list_snapshot" = Will contain previous state of list. Used for removing extra rows on list update

			PROCESS:
			1 - Fetch Data and build rows "buildList()"
			2 - Call scrape API to activate data scraping
			3 - Edit Item - to edit item's detail (still in progress)
			4 - Delete Item - Send item id to delete URL


			NOTES:
			-- Add event handlers to "edit", "delete"
			-- Remove extra data on re-render
			-- CSRF Token
		*/

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var activeItem = null
var list_snapshot = []


function buildList(){
    var wrapper = document.getElementById('list-wrapper')
    //wrapper.innerHTML = ''
    var load = document.getElementById('loading');

    var url = '/api/property'
    load.innerHTML = `<div class="loader" id="loader"></div>`

    fetch(url)
    .then((resp)=>resp.json())
    .then(function(data){
        console.log('Data:', data)

        var list = data
        for (var i in list){

            try{
                document.getElementById(`data-row-${i}`).remove()
            }catch(err){

            }

            var title = `<small><span class="title">${list[i].names} </span></small>`
            var links = `<small><a href="${list[i].links}">links</a></small>`
            var states = `<small>${list[i].states}</small>`
            var prices = `<small>RM${list[i].prices}</small>`
            var bedrooms = `<small>Rooms:${list[i].bedrooms} </small>`
            var bathrooms = `<small>Toilet:${list[i].bathrooms} </small>`
            var built_ups = `<small>${list[i].built_ups}sqft </small>`
            var built_years = `<small>${list[i].built_years} </small>`
            var house_types = `<small>${list[i].house_types} </small>`
            var furnishings = `<small>${list[i].furnishings} </small>`
            var prices_per_sqft = `<small>RM${list[i].prices_per_sqft}/sqft </small>`
            var images = `<img src="${list[i].images}" alt="opss" style="width:100px;height:100px;">`


            var item = `
                <div id="data-row-${i}" class="task-wrapper flex-wrapper">
                    <div style="flex:2">
                        ${images}
                    </div>
                    <div style="flex:1">
                        ${title}
                    </div>
                    <div style="flex:1">
                        ${links}
                    </div>
                    <div style="flex:1">
                        ${states}
                    </div>
                    <div style="flex:1">
                        ${prices}
                    </div>
                    <div style="flex:1">
                        ${bedrooms}
                    </div>
                    <div style="flex:1">
                        ${bathrooms}
                    </div>
                    <div style="flex:1">
                        ${built_ups}
                    </div>
                    <div style="flex:1">
                        ${built_years}
                    </div>
                    <div style="flex:1">
                        ${house_types}
                    </div>
                    <div style="flex:1" class="text-center">
                        ${furnishings}
                    </div>
                    <div style="flex:1">
                        ${prices_per_sqft}
                    </div>
                    <div style="flex:1">
                        <button class="btn btn-sm btn-outline-info edit">Edit </button>
                    </div>
                    <div style="flex:1">
                        <button class="btn btn-sm btn-outline-dark delete">Delete</button>
                    </div>
                </div>

            `
            wrapper.innerHTML += item

        }

        if (list_snapshot.length > list.length){
            for (var i = list.length; i < list_snapshot.length; i++){
                document.getElementById(`data-row-${i}`).remove()
            }
        }

        list_snapshot = list

        for (var i in list){
            var editBtn = document.getElementsByClassName('edit')[i]
            var deleteBtn = document.getElementsByClassName('delete')[i]

            editBtn.addEventListener('click', (function(item){
                return function(){
                    editItem(item)
                }
            })(list[i]))

            deleteBtn.addEventListener('click', (function(item){
                return function(){
                    deleteItem(item)
                }
            })(list[i]))

        }
    load.innerHTML = `<div class="hide-loader" id="loader"></div>`
    });

}

function scrape(){
    var load = document.getElementById('loading');
    load.innerHTML = `<div class="loader" id="loader"></div>`
    var url = '/api/scraping';
    var formData = new FormData();
    formData.append("check", "secret");
    formData.append("csrfmiddlewaretoken", csrftoken);
    fetch(url, {
        method:'POST',
        body:formData,
        })
    .then(function(){
        buildList()
    })
}


function editItem(item){
    alert('sorry this feature is under development');
    console.log('Item clicked')
    fetch(`/api/property/${item.id}`, {
        method:'GET',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        }
    }).then((response) => {
    })
}


function deleteItem(item){
    console.log('Delete clicked')
    fetch(`/api/property/${item.id}`, {
        method:'DELETE',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        }
    }).then((response) => {
        buildList()
    })
}


function alert1(){
 alert('ops, you are not authorised to do so');
}

