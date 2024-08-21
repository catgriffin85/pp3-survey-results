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
    Provides survey question to user and requests a response.
    Response is checked and if valid the next question will show.
    If response is invalid and error message and another attempt
    will be presented.
    """
    print('How would you rate your overall experience at Bunratty Castle?')
    print('1 = Very Poor, 2 = Poor, 3 = Neutral, 4 = Good, 5 = Excellent\n')

    answer_one = input("Please enter your answer here: \n").strip()
    while answer_one == '' or is_input_not_valid(answer_one):
        answer_one = input('Invalid input! Please try again: ').strip()
    
    print('\nHow would you rate the quality of customer service provided?')
    print('1 = Very Poor, 2 = Poor, 3 = Neutral, 4 = Good, 5 = Excellent\n')

    answer_two = input("Please enter your answer here: \n").strip()
    while answer_two == '' or is_input_not_valid(answer_two):
        answer_two = input('Invalid input! Please try again: ').strip()

    print('\nHow likely are you to recommend this attraction to a friend?')
    print('1= Not at All, 2= Unlikely, 3= Maybe, 4= Likely, 5= Very Likely\n')

    answer_three = input("Please enter your answer here: \n").strip()
    while answer_three == '' or is_input_not_valid(answer_three):
        answer_three = input('Invalid input! Please try again: ').strip()

    return int(answer_one), int(answer_two), int(answer_three)


def is_input_not_valid(answer):
    """
    This checks the answer to ensure it is between 1 and 5
    and returns a Boolean True or False that is used to validate
    the users answer.
    """
    RESPONSES = ['1', '2', '3', '4', '5']
    if answer in RESPONSES:
        return False
    return True


def add_to_results_worksheet(data):
    """
    Adds survey results to the results tab on the
    Google Sheet worksheet.
    """
    results_worksheet = SHEET.worksheet('results')
    results_worksheet.append_row(data)


def count_input_in_column(input_value, column_index):
    results = SHEET.worksheet('results').get_all_values()
    
    column_values = [row[column_index] for row in results if row[column_index].isdigit()]

    column_values = [int(value) for value in column_values]

    count_user_input = column_values.count(input_value)

    total_responses = len(column_values)

    answer_percentage = round(count_user_input / total_responses * 100)

    return count_user_input, answer_percentage


def question_one_result(input_value):
    column_index = 0

    count_user_input, answer_percentage = count_input_in_column(input_value, column_index)

    ##print(f'Input {answer_one}. Count of input: {count_user_input}')
    
    print(f'\n{answer_percentage}% of visitors also rated their experience as a "{answer_one}"')


def question_two_result(input_value):
    column_index = 1

    count_user_input, answer_percentage = count_input_in_column(input_value, column_index)

    ##print(f'Input {answer_two}. Count of input: {count_user_input}')
    
    print(f'{answer_percentage}% of visitors also rated our customer service as a "{answer_two}"')


def question_three_result(input_value):
    column_index = 2

    count_user_input, answer_percentage = count_input_in_column(input_value, column_index)

    if input_value == 1:
        answer = 'not at all likely'
    elif input_value == 2:
        answer = 'unlikely'
    elif input_value == 3:
        answer = 'maybe likely'
    elif input_value == 4:
        answer = 'likely'
    else:
        answer = 'very likely'

    ##print(f'Input {answer_three}. Count of input: {count_user_input}')
    
    print(f'{answer_percentage}% of visitors are also {answer} to recommend Bunratty Castle\n')


def welcome_message():
    """
    Welcome message for the user before starting the survey.
    """
    print('\nThank you for visiting Bunratty Castle today.')
    print('We value your opinion and would love to hear your thoughts!')
    print('Could you please spare a few minutes to complete this survey?\n')


def closing_message():
    """
    Closing message for the user once they have completed the survey.
    """
    print('\nThank you for taking the time to complete our survey!\n')
    print('Take a look below at how other visitors rated their experience.')


if __name__ == '__main__':
    welcome_message()
    survey_responses = survey_feedback()

    answer_one, answer_two, answer_three = survey_responses

    add_to_results_worksheet(list(survey_responses))

    closing_message()

    input_value_one = answer_one
    input_value_two = answer_two
    input_value_three = answer_three

    question_one_result(input_value_one)
    question_two_result(input_value_two)
    question_three_result(input_value_three)
