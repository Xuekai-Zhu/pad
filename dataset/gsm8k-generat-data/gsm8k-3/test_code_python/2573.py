def solution():
    """Bill composes 20 total math questions for money.  Ryan composes twice as many problems as Bill, and Frank composes 3 times as many as Ryan.  Assuming each person has to compose 4 different types of math problems in equal proportion out of the total amount, how many problems of each type does Frank compose?"""
    # Define the total number of math questions
    total_questions = 20

    # Define the number of math questions each person composes
    bill_questions = total_questions / 4
    ryan_questions = 2 * bill_questions
    frank_questions = 3 * ryan_questions

    # Calculate the number of problems of each type Frank composes
    type1_questions = frank_questions / 4
    type2_questions = frank_questions / 4
    type3_questions = frank_questions / 4
    type4_questions = frank_questions / 4

    # Display the number of problems of each type Frank composes
    result = (type1_questions, type2_questions, type3_questions, type4_questions)
    return result

print(solution())