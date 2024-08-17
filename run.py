import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('survey_results')

print('Thank you for visiting Bunratty Castle today.')
print('We value your opinion and would love to hear your thoughts!')
print('Could you please spare a few minutes to complete this survey?\n')

def survey_feedback():
    """
    Get answer survey questions from the user
    """
    print('How would you rate your overall experience at Bunratty Castle today?')
    print('1 = Poor, 5 = Excellent\n')

    answer_one = input("Please enter your answer here: ")

    print('\nHow would you rate the quality of customer service provided by the staff?')
    print('1 = Very Poor, 5 = Excellent\n')

    answer_two = input("Please enter your answer here: ")

    print('\nHow likely are you to recommend this attraction to a friend or family member?')
    print('1 = Not Likely, 5 = Very Likely\n')

    answer_three = input("Please enter your answer here: ")

    return answer_one, answer_two, answer_three

responses = survey_feedback()

print(responses)


    


