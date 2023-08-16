document.querySelectorAll('.topic-card').forEach(item => {
    item.addEventListener('click', event => {
        let subjectName = event.currentTarget.querySelector('.topic-name').textContent;
        let userName = "hina"

        console.log(`Clicked on subject: ${subjectName}`);

        document.querySelectorAll('.topic-card.selected').forEach(selectedItem => {
            selectedItem.classList.remove('selected');
        });

        event.currentTarget.classList.add('selected');

fetch('http://127.0.0.1:5001/study_plan', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        username: userName,
        subject: subjectName
    })
})
.then(response => response.json())
.then(data => console.log(data))   // Added this to log the response from the server
.catch((error) => {
  console.error('Error:', error);
});



document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      events: '/get_events'  // Assuming you have an endpoint at '/get_events' that returns the events
    });

    calendar.render();
});

// Downloading a presentation

document.addEventListener('DOMContentLoaded', function() {
    // Downloading a presentation
    $('#generate-button').click(function(e) {
        e.preventDefault();
        // Show the loading indicator
        $('#loading-indicator').show();
        // Hide the Generate button
        $(this).hide();
        // Disable the form inputs
        $('#generate-form').find('input, textarea, button').attr('disabled', 'disabled');
        // Submit the form manually
        $('#generate-form').submit();
    });
});

// Load indicator

document.getElementById('generate-form').addEventListener('submit', function() {
     document.getElementById('loading-indicator').style.display = 'block';
});

