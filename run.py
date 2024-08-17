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
print('Could you please spare a few minutes to complete this survey?')

def survey_feedback_first_question():
    """
    Get answer to the first survey question from the user
    """
    print('How would you rate your overall experience at Bunratty Castle today?')
    print('1 = Poor, 5 = Excellent')

    answer_one = input("Please enter your answer here: ")

    return answer_one

response_one = survey_feedback_first_question()

