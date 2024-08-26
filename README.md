# Bunratty Castle Customer Experience Survey

Bunratty Castle Customer Experience Survey is a survey provided to recent visitors of the castle that is run in Heroku. The survey is used to gather feedback from visitors with the aim of helping management at Bunratty Castle identify areas that are going well and areas that may need improvement. 

You can view the Herku terminal [here](https://survey-results-pp3-fc6036f74caa.herokuapp.com/)

![Heroku](/assets/images/heroku-terminal.png)

## Purpose

The purpose of this survey is to:
* <strong>Assess Visitor Satisfaction:</strong> It helps management understand how visitors feel about their experience, including the customer service they received and the likelyhood of them recommending Bunratty Castle to a friend. 

* <strong>Enhance Visitor Experience:</strong> By analysing feedback, management can implement changes that align with visitor expectations making the attaction much more appealing and enjoyable. 

## User Experience

<strong>Project Goals</strong>

As the survey owner, I want the program to:

* encourage visitors to the attraction to take the survey.
* provide clear instructions on how the feedback should be provided.
* validate the user inputs to ensure the data provided is accurate and can be used for analysis.
* collect inputs provided by users on a google sheet.
* use the data collected on the google sheet to calculate response numbers and percentages.
* provide the user with feedback on how their responses compare with other responses we have received.
* as a 'thank you' for completing the survey, offer to enter the user into a draw for free passes.
* validate the users email address if they do want to enter the draw.
* thank the user for completing the survey.

As the user, I want the program to:

* explain which attraction the survey is referring to.
* provide information on how I should answer the questions asked.
* allow me to enter my responses easily.
* provide me with information on surevey results.
* reward me for completing the survey.
* thank me for my time.

## Flowchart Plan

During the planning stages, I created a flowchart to help me visualise how I wanted the survey to work and what checks I wanted to do. The flow chart was created using [Lucidchart](https://www.lucidchart.com/pages/).

Inititally when planning my project I felt my idea for a survey was not too complex but once I started mapping it out it helped me identify areas that would need more thought such as validation, calculations and how to end the survey.

![Lucid flow chart](/assets/images/plan.png)

## Data Storage (Google Sheets)

Both the survey answers and the users email address was stored in the google sheet. The calculation for survey results used the data collected the the google sheet. You can veiw the sheet [here](https://docs.google.com/spreadsheets/d/1braNOvh9GAhV9h-CeiLNWs9XDPU58KwQL3b_o4m4Tuc/edit?gid=0#gid=0)

## Features

The design and display of the survey is limited due to the fact that it is using python only and the Heroku terminal size. If this was a real life survey an interface other than a command line could be incorporated which would provide a better user experience. 

The survey is intended to be used only once per user so an option to complete the survey again is not provided to the user. 

### Welcome Section

The terminal opens with the welcome section. This section thanks the user for visiting Bunratty Castle and requests that the user completed a survey.

The first question is displayed with the welcome message.

![Welcome Section](/assets/images/welcome-section.png)

### Questions Section

The questions section is made up of 3 questions for the user to answer. Each question gives the user the option to input a number between 1 and 5 depending on the users experience. Each number is explained to the user. 

Through validation the user is able to move on only when they have input an number between 1 and 5. Additional spaces are stripped out using code. Numbers less than 1 or greater than 5 and letters will not be accepted. The user will be advised via an error message that they have entered an invalid input and asked to try again. Once the correct input has been entered the next question will display.

Once all 3 questions have been entered a thank you message will display to the user.

![Questions Section](/assets/images/question-section.png)

### Results Section

Once all questions have been answered and the thank you message has been displayed the user will be provided with surevey results that let them know how many other people answered the survey the same as them and the % to the total number of survey responses. 

For example: if a user has entered "5" for "excellent" as their answer to the first question they will be show the % of people who also answered "excellent" to that question as well as the total number of people who answered the same. 

This is reapeated for each of the three questions. 

![Results Section](/assets/images/results-section.png)

### Draw Section

After the survey results have been displayed to the user, they will be offered an opportunity to be entered into a draw to win 2 free passes to Bunratty Castle. The user must input "Y" or "N" to indicate if they would like the opportunity to win the passes.

If the users enters a lowercase "Y" or "N" it will be converted to upperase and be accepted. However, if they user enters any other letter or a number then they will be advised that their input is invalid and asked to enter a "Y" or "N".

Once the correct input has been entered the user will be able to progress. 

If the user enters "N", they will be thanked for their response and no futher messages are displayed.

If the user enters "Y", they will be asked to input their email address. Using code taken from [Geeks for Geeks website](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python) and in re import email validation has been set up. The user must enter a valid email address to continue. Once the email address has been validated the user will be thanked and confirmation that they have been entered into the draw is displayed.

![Draw Section](/assets/images/draw-section.png)

## Technology Used

* Python to write my programme.
* JavaScript provided in the Code Institute template.
* CSS provided in the Code Institute template.
* HTML provided in the Code Institute template.
* Google sheets to store the information.
* [Heroku](https://www.heroku.com/) to deploy the project

## Python Libraries Used

* [gspread](https://docs.gspread.org/en/latest/) to link my google sheet so the survey answers could be stored.
* [re](https://www.w3schools.com/python/python_regex.asp#:~:text=Python%20has%20a%20built%2Din,import%20re) to allow me to work with Regular Expressions when validating the email address input.

## Testing

I tested my project by doing the following:

1. Passed the code through a PEP8 linter and fixed all errors.
2. Tried invalid inputs to all input choices and made sure error messages were displayed.
3. Completed all input tests in my local terminal and the Heroku terminal.

### PEP8 Linter Testing:

When I first used the PEP8 validator on my code, a few errors were identified:

* Line too long
    * This error was raised as a result of certain lines of code being too long.
    * I resolved this by reviewing each line and shortening the code. Some print statement lines were long as they contained f strings with variables and text. To reduce the length of these lines I created a message variable which contained the text. This helped shorten these lines. For lines that contained just code, I broke it up over two lines and this worked as long as the break was within braces.

* Blank line contains white space
    * This is a self explanatory warning and was resolved by removing the white space on blank lines.

* Trailing whitespace
    * This is also self explanatory and was resolved by removing the white space at the end of the lines that were flagged.

Once these issues were resovled, no errors were shown for my code.

![CI Python Linter Results](/assets/images/ci-python-linter-results.png)

### Input Testing

<u>Test 1 - Question 1 Input</u>

For this first test of the input on question one the expected behaviour is that the user input will only be accepted if it is 1, 2, 3, 4 or 5. It can have spaces at either side but it cannot be blank, contain a number less than 1 or greater than 5 and it cannot contain letters. If an invalid input is entered an error message will be displayed saying "Invalid input! Please try again:" and the user will get another opportunity to input their answer. Validation will continue until the correct input has been entered. Once the correct input has been entered the next question will be displayed.

![Test 1 Gitpod Terminal](/assets/images/test-one-gitpod-terminal.png)

![Test 1 Heroku Terminal](/assets/images/test-one-heroku-terminal.png)

<u>Test 2 - Question 2 Input</u>

This second test is run exactly the same as the first test. The same behaviour is expected and the same validation is in place.

![Test 2 Gitpod Terminal](/assets/images/test-two-gitpod-terminal.png)

![Test 2 Heroku Terminal](/assets/images/test-two-heroku-terminal.png)

<u>Test 3 - Question 3 Input</u>

This third test is run exactly the same as the first and second tests. The same behaviour is expected and the same validation is in place. Once the correct input has been entered a thank you message will be displayed and then the survey results and option to enter a draw.

![Test 3 Gitpod Terminal](/assets/images/test-three-gitpod-terminal.png)

![Test 3 Heroku Terminal](/assets/images/test-three-heroku-terminal.png)

<u>Test 4 - Inputs Adding to Google Sheet</u>

Once I know my inputs are valid, I need to check that the data is flowing through to the google sheet. To check this, I opened the [Google Sheet](https://docs.google.com/spreadsheets/d/1braNOvh9GAhV9h-CeiLNWs9XDPU58KwQL3b_o4m4Tuc/edit?gid=0#gid=0) and scrolled to the last line of information. It matches the last entry into the survey so the input is being added to my Google Sheet.

![Google Sheet Input](/assets/images/google-sheet-check-input.png)

<u>Test 5 - Survey Results</u>

There are three parts to the testing for the Survey Results section.

1. Check if the survey results reference the correct input.
2. Check the number of people displayed in the results is correct.
3. Check the % calculation for each line is correct.

For the example in the print screen: 

<u>Correct Input</u>

* Question one input was "3" which is "average". The first line of the survey results advises of other visitors who rated their experience as "average". This is correct so the input referenced is correct.

* Question two input was "4" which is "good". The second line of the survey results advises of other visitors who rated the customer service as "good". This is correct so the input referenced is correct.

* Question three input was "4" which is "likely". The third line of the survey results advises of other visitors who are "likely" to recommend to a friend. This is correct so the input referenced is correct. 

<u>Correct Count of People</u>

* Line one of the survey results displays that 26 people also rated their experience as average. To validate this number I opened the google sheet that stores the data and applied a filter. I filtered question one answers by "3" and did a count. The count confirmed that 3 has been entered 26 times into the survey. So the information displayed in the survey results is correct and the count is being applied to the correct column in the google sheet.

![Google Sheet Filter Question 1](/assets/images/google-sheet-q1-filter.png)

* Line two of the survey results displays that 34 people also rated the customer service as good. To validate this number I again used the google sheet that stores the data and applied a filter. I filtered question two answers by "4" and did a count. The count confirms that 4 has been entered 34 times into the survey. So the information displayed in the survey results is correct and the count is being applied to the correct column in the google sheet.

![Google Sheet Filter Question 2](/assets/images/google-sheet-q2-filter.png)

* Line three of the survey results displays that 32 people also likely to recommend Bunratty Castle to a friend. To validate this number I again used the google sheet that stores the data and applied a filter. I filtered question three answers by "4" and did a count. The count confirms that 4 has been entered 32 times into the survey. So the information displayed in the survey results is correct and the count is being applied to the correct column in the google sheet.

![Google Sheet Filter Question 3](/assets/images/google-sheet-q3-filter.png)

<u>% Calculation Check</u>

To validate the % provided in the survey results, I did a total count of the entries in the google sheet. At the time of testing, there were 91 entries.

* Line one: 26 people divided by 91 total entries = 29%. 
* Line two: 34 people divided by 91 total entries = 37%.
* Line three: 32 people divided by 91 total entries = 35%

All % displayed in the survey results are correct. 

![Google Sheet Total Entries](/assets/images/google-sheet-total-entries.png)

<u>Test 6 - Option to Enter Draw</u>

After the survey results are displayed another message will allow appear offering the change to win 2 free day passes. The user must enter either "Y" or "N". Validation has been set up on this input which allows the user to enter either "Y", "N", "y" or "n". Any other input will result in an error message advising the user "Invalid input! Please enter Y or N:" 

If the user enters "Y" or "y" the input will be accepted and they will then be asked to provide an email address. 

![Test 6 Gitpod Terminal - Yes](/assets/images/test-six-gitpod-terminal.png)

![Test 6 Heroku Terminal - Yes](/assets/images/test-six-heroku-terminal.png)

If the user enters "N" or "n" the input will be accepted and "Thank you for your response!" will display and no more inputs are required.

![Test 6 Gitpod Terminal - No](/assets/images/test-six-gitpod-terminal-no.png)

![Test 6 Heroku Terminal - No](/assets/images/test-six-heroku-terminal-no.png)

The survey will not begin again and the user will not be asked if they would like to complete another survey. As it is a customer experience survey based off of one specific visit only one survey response is required per user.

<u>Test 7 - Email Address Validation</u>

If the users decides to input "Y" or "y" and sees the "Please provide your email address: " input message they must enter a valid email address. 

To validate the email address I took some code from [Geeks for Geeks](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python) website. This checked if the input was in the correct format. 

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

The code checks for that the following format is used:

* The first part of the input contains uppercase or lowercase letters between a and z or numbers between 0 and 9 or a . _ % + or -
* Next it checks for an @ symbol
* After this is checks if the next part of the input contains uppercase or lowercase letters between a and z or numbers between 0 and 9 or a . or _
* Next it checks for a .
* Lastly it checks that the input after the . contains uppercase or lowercase letters between a and z and is between 2 and 7 letters in length

I tested different variations of invalid email address to check my validation was working. When an incorrectly formatted email address was entered an message displayed advising "Please provide a valid email address: " and the user could try again.

Once a valid email address was entered "Thank you. You have now been entered into our draw!" is displayed. No other inputs are required. The survey is over.

![Test 7 Gitpod Terminal](/assets/images/test-seven-gitpod-terminal.png)

![Test 7 Heroku Terminal](/assets/images/test-seven-heroku-terminal.png)

<u>Test 8 - Email Address Adding to Google Sheet</u>

The last test for this project is to check if the valid email entered has been added to the [Google Sheet](https://docs.google.com/spreadsheets/d/1braNOvh9GAhV9h-CeiLNWs9XDPU58KwQL3b_o4m4Tuc/edit?gid=1991835168#gid=1991835168). And to also check that the invalid email address have not been added to the sheet.

Once again I open my google sheet and check the last entry. Only the valid email address has been added. 

![Test 8 Google Sheet](/assets/images/google-sheet-check-email-address.png)