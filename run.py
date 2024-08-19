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


def survey_feedback():
    """
    Get answer survey questions from the user
    """
    print('How would you rate your overall experience at Bunratty Castle?')
    print('1 = Very Poor, 2 = Poor, 3 = Neutral, 4 = Good, 5 = Excellent\n')

    answer_one = input("Please enter your answer here: ").strip()
    while answer_one == '' or is_input_not_valid(answer_one):
        answer_one = input('Invalid input! Please enter a number between 1 and 5: ').strip()

    print('\nHow would you rate the quality of customer service provided?')
    print('1 = Very Poor, 2 = Poor, 3 = Neutral, 4 = Good, 5 = Excellent\n')

    answer_two = input("Please enter your answer here: ").strip()
    while answer_two == '' or is_input_not_valid(answer_two):
        answer_two = input('Invalid input! Please enter a number between 1 and 5: ').strip()

    print('\nHow likely are you to recommend this attraction to a friend?')
    print('1 = Very Unlikely, 2 = Unlikely, 3 = Neutral, 4 = Likely, 5 = Very Likely\n')

    answer_three = input("Please enter your answer here: ").strip()
    while answer_three == '' or is_input_not_valid(answer_three):
        answer_three = input('Invalid input! Please enter a number between 1 and 5: ').strip()

    print('\nThank you for taking the time to complete our survey!\n')

    return answer_one, answer_two, answer_three
 

def is_input_not_valid(answer):
    """
    This checks the answer to ensure it is between 1 and 5
    and returns a Boolean True or False
    """
    RESPONSES = ['1', '2', '3', '4', '5']
    if answer in RESPONSES:
        return False
    return True


def add_to_results_worksheet(data):
    """
    Adds survey results to the google sheet worksheet
    """
    results_worksheet = SHEET.worksheet('results')
    results_worksheet.append_row(data)


def welcome_message():
    """
    Welcome message for the user before starting the survey
    """
    print('Thank you for visiting Bunratty Castle today.')
    print('We value your opinion and would love to hear your thoughts!')
    print('Could you please spare a few minutes to complete this survey?\n')


if __name__ == '__main__':
    welcome_message()
    survey_responses = survey_feedback()

    answer_one, answer_two, answer_three = survey_responses

    add_to_results_worksheet(list(survey_responses))

    print(survey_responses)







    


