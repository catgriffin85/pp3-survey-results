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

