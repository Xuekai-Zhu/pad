def solution():
    """Bill composes 20 total math questions for money. Ryan composes twice as many problems as Bill, 
    and Frank composes 3 times as many as Ryan. Assuming each person has to compose 4 different types of math 
    problems in equal proportion out of the total amount, how many problems of each type does Frank compose?"""
    total_questions = 20
    bill_questions = total_questions // 7
    ryan_questions = 2 * bill_questions
    frank_questions = 3 * ryan_questions
    problems_per_type = total_questions // 4
    frank_type1 = frank_questions // 4
    frank_type2 = frank_questions // 4
    frank_type3 = frank_questions // 4
    frank_type4 = frank_questions - (frank_type1 + frank_type2 + frank_type3)
    result = (frank_type1, frank_type2, frank_type3, frank_type4)
    return result

print(solution())