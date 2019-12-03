var correctAnswers = 0;
var button = document.getElementsByClassName('answer-button');

function counter(variant, answer) {

               
if(variant === answer) {
    
correctAnswers++;
console.log(correctAnswers);
    
}

return correctAnswers;
    
}


function disableButton(button) {

button.disabled = true;

    
}


function showResult(answers) {

document.getElementById('correctAnswersAmount').innerHTML = correctAnswers + ' of 10';
    
}