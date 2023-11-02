def solution():
    total_questions = 20  # Bill composes 20 total math questions
    bill_questions = total_questions / 7  # Bill composes 4 types of math problems in equal proportion out of the total amount
    ryan_questions = 2 * bill_questions  # Ryan composes twice as many problems as Bill
    frank_questions = 3 * ryan_questions  # Frank composes 3 times as many as Ryan

    # Calculate the number of problems of each type Frank composes
    type1 = frank_questions / 4
    type2 = frank_questions / 4
    type3 = frank_questions / 4
    type4 = frank_questions / 4
    result = (type1, type2, type3, type4)
    return result

print(solution())