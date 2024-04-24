function startWebcam() {
    $.ajax({
        url: '/start-webcam',
        type: 'GET',
        success: function(response) {
            console.log('Webcam started successfully');
        },
        error: function(xhr, status, error) {
            console.error('Error starting webcam:', error);
        }
    });
}
