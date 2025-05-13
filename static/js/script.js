$(document).ready(function() {
  // Bind click event for expandable boxes.
  $('.box-header').on('click', function() {
    $(this).next('.box-content').slideToggle();
  });
});

// Function called when an OK button is clicked.
function submitForm(functionCall, button) {
  // Locate the parent command box container.
  var commandBox = $(button).closest('.command-box');
  var valuesList = [];

  // Iterate over all input elements in the command box in DOM order.
  commandBox.find('input').each(function() {
    var type = $(this).attr('type');
    var name = $(this).attr('name');
    if (type === 'text') {
      // For text inputs, push their value.
      valuesList.push($(this).val());
    } else if (type === 'radio') {
      // For radio buttons, push the value only if it is checked.
      if ($(this).is(':checked')) {
        valuesList.push($(this).val());
      }
    } else if (name === 'droplist') {
      // For dropdowns, push the selected value.
      var selectedValue = $(this).find('option:selected').val();
      alert(selectedValue);
      if (selectedValue) {
        valuesList.push(selectedValue);
      }

    }
  });

  // Prepare the payload with the function call string and the list of input values.
  var payload = {
    functionCall: functionCall,
    data: valuesList
  };

  // Send the payload to the Flask backend via AJAX.
  $.ajax({
    url: '/submit',
    method: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(payload),
    success: function(response) {
      console.log('python returned: ', response);
      // Display the result in a simple message box (alert)
      alert(response.result);
    },
    error: function(err) {
      console.error('Submission failed. This is the error returned :', err);
    }
  });
}
