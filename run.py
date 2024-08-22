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
    results_worksheet = SHEET.worksheet("results")
    results_worksheet.append_row(data)


def count_input_in_column(input_value, column_index):
    """
    Gets the survey values from the results tab on the google sheet
    to be used in the calculation for survey results.
    Creates a variable for the column index so the correct column
    is reference for each survey question when calculating results.
    """
    results = SHEET.worksheet('results').get_all_values()

    column_values = [row[column_index] for row in results if row[column_index].isdigit()]

    column_values = [int(value) for value in column_values]

    count_user_input = column_values.count(input_value)

    total_responses = len(column_values)

    answer_percentage = round(count_user_input / total_responses * 100)

    return count_user_input, answer_percentage


def question_one_result(input_value):
    """
    Provides the column index to check the user input against for
    question one and calculates the answer percentage using the
    user input for question one
    """
    column_index = 0

    count_user_input, answer_percentage = count_input_in_column(input_value, column_index)

    print(f'\n{answer_percentage}% of visitors also rated their experience as a "{answer_one}"')


def question_two_result(input_value):
    """
    Provides the column index to check the user input against for
    question two and calculates the answer percentage using the
    user input for question two
    """
    column_index = 1

    count_user_input, answer_percentage = count_input_in_column(input_value, column_index)

    print(f'{answer_percentage}% of visitors also rated our customer service as a "{answer_two}"')


def question_three_result(input_value):
    """
    Provides the column index to check the user input against for
    question three and calculates the answer percentage using the
    user input for question three. Assigns text to answer variable
    to be used in print statement depending on user input.
    """
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


def competition_option():
    """
    This offers the user the option to enter a draw if they
    provide their email address.
    """
    print('Would you like to enter a draw for free day passes?')
    competition_entry = input('Enter Y for Yes or N for No here: \n').strip()

    while competition_entry == '' or competition_entry_invalid(competition_entry):
        competition_entry = input('Invalid input! Please enter Y or N: \n').strip()

    if competition_entry == "Y":
        email_address = input('\nPlease provide your email address: \n')
        print('\nThank you. You have now been entered into our draw!')
        return email_address
    else:
        print('\nThank you for your response!')
        return None


def competition_entry_invalid(answer):
    """
    This validates the user input in relation to entry of a
    competition and provides a Boolean True of False.
    """
    COMPETITION = ['Y', 'N']
    if answer in COMPETITION:
        return False
    return True


def add_email_to_worksheet(data):
    """
    If the user inputs an email address for the draw it is
    added to the email tab on the google sheet
    """
    email_worksheet = SHEET.worksheet("email")
    email_worksheet.append_row(data)


def update_worksheet(data, worksheet):
    """
    Updates the correct worksheet with the data provided.
    Used function from Love Sandwiches project runthrough.
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)


if __name__ == '__main__':
    welcome_message()
    survey_responses = survey_feedback()

    answer_one, answer_two, answer_three = survey_responses

    update_worksheet(survey_responses, "results")

    closing_message()

    input_value_one = answer_one
    input_value_two = answer_two
    input_value_three = answer_three

    question_one_result(input_value_one)
    question_two_result(input_value_two)
    question_three_result(input_value_three)

    email_address = competition_option()

    if email_address:
        update_worksheet([email_address], "email")
