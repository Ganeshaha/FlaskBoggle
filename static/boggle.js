 
 score = 0
 
 $("#guess-form").on("submit",
    async function handleFormSubmit(event) {
        event.preventDefault();
        //console.log(event.target[0].value);

        validWordResponse = await axios.post('/submit',
            {value: event.target[0].value}
        ).then(response => savedReponse = response);

        result = savedReponse.data.result;
        console.log(result)
        

        if (result == "ok"){
            $("#show-result").text("Your word is valid and exists on the board!")

            score += event.target[0].value.length
            
            
        }
        else if (result == "not-on-board"){

            $("#show-result").text("Your word is valid but does not exist on the board.")
        }
    
        else if (result == "not-word"){

            $("#show-result").text("That is not a word.")
        }
        $("#show-result").text(`Score: ${score}`)
        
        
    }
)
currentTime = 10;
let timerInterval = setInterval(showTime, 1000);
async function showTime(){
    $("#timer").text(`Time Left: ${currentTime}`);
    

    if (currentTime<=0){
        $('#submit-button').hide()
        $("#timer").text(`Time Left: ${currentTime}. You cannot make any more guesses`);
        scoreResponse = await axios.post('/score',
            {score: score}
        ).then(response => savedReponse = response);

        console.log(savedReponse)
        clearInterval(timerInterval);
    }
    currentTime--;




}