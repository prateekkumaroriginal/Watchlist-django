// $('input[type=radio]').on('change', function() {
//     $(this).closest("form").submit();
// });

document.addEventListener('click', function(e){
    if(e.target.closest('.dropdown-menu') && e.target.nodeName.toLowerCase() === 'button'){
        e.preventDefault();
        var form = target.closest('form');
        var form_data = new FormData(form);
        form_data.append(target.name, target.value);
        fetch(
            form.action,
            {
                method: 'post',
                body: form_data,
            }
        ).then(function(response) {
            return response.json();
        })
        .then(function(json) {
            // do stuff here
        });
    }
}, false);