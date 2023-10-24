// Function to show the modal
function showModal() {
    var modal = document.getElementById('modal-generate');
    modal.style.display = 'block';
}

// Function to hide the modal
function hideModal() {
    var modal = document.getElementById('modal-generate');
    modal.style.display = 'none';
}

// Event listener for the "Generate" button
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('generate-button').addEventListener('click', function(e) {
        e.preventDefault();  // Prevent the default form submission
        showModal();  // Show the modal


        // Serialize form data and send it to the server via an AJAX POST request
        const formData = new FormData();
        formData.append('presentation_title', document.getElementById('presentation_title').value);
        formData.append('presenter_name', document.getElementById('presenter_name').value);
        formData.append('number_of_slide', document.getElementById('number_of_slide').value);
        formData.append('user_text', document.getElementById('user_text').value);
        formData.append('insert_image', document.getElementById('insert_image').checked);

        const template_choice = document.querySelector('input[name="template_choice"]:checked').value;
        formData.append('template_choice', template_choice);
        // ... append other form data similarly
        console.log([...formData]);  // Check the logged output to ensure the data is correct
        fetch('/generator', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();  // This assumes the server will return JSON
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});


