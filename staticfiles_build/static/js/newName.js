let hintCounter = 0;

document.getElementById("addHint").addEventListener("click", function(event){
    event.preventDefault();  // prevent form submission

    hintCounter++;

    const formGroupDiv = document.getElementById("hints").querySelector(".form-group");

    // Create new div to hold hint fields
    const newHintDiv = document.createElement("div");
    newHintDiv.setAttribute("id", "hint" + hintCounter + "-group");
    newHintDiv.setAttribute("class", "hint-group d-flex"); // d-flex will make the elements display in line

    // Create new input field
    const newHintInput = document.createElement("input");
    newHintInput.setAttribute("type", "text");
    newHintInput.setAttribute("class", "form-control hint-input"); // assign it a class
    newHintInput.setAttribute("id", "hint" + hintCounter);
    newHintInput.setAttribute("name", "hint_" + hintCounter);
    
    // Create new remove button
    const removeButton = document.createElement("button");
    removeButton.setAttribute("type", "button");
    removeButton.setAttribute("class", "btn btn-secondary remove-hint");
    removeButton.setAttribute("style", "background-color: #67b2c9;");
    removeButton.innerText = "Remove";

    // Append input field and button to the new hint div
    newHintDiv.appendChild(newHintInput);
    newHintDiv.appendChild(removeButton);

    // Append the new hint div to the form group div inside hints div
    formGroupDiv.appendChild(newHintDiv);

    // Event listener for the remove button
    removeButton.addEventListener("click", function() {
        formGroupDiv.removeChild(newHintDiv);
    });
});


