$(document).ready(function() {
    $('#uploadForm').submit(function(event) {
        event.preventDefault();
        
        var formData = new FormData();
        formData.append('image', $('#imageInput')[0].files[0]);
        
        $.ajax({
            type: 'POST',
            url: '/',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                $('#result').text(response);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });
});
