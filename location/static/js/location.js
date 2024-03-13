$(document).ready(function() {
    $('#getLocationBtn').on('click', function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                $('#latitudeInput').val(position.coords.latitude);
                $('#longitudeInput').val(position.coords.longitude);
                $('#locationForm').show();
            }, function(error) {
                $('#errorMsg').text('Error: ' + error.message).show();
            });
        } else {
            $('#errorMsg').text('Error: Geolocation is not supported by this browser.').show();
        }
    });
});
