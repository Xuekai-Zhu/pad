def solution():
    """Bill composes 20 total math questions for money. Ryan composes twice as many problems as Bill, and Frank composes 3 times as many as Ryan. Assuming each person has to compose 4 different types of math problems in equal proportion out of the total amount, how many problems of each type does Frank compose?"""
    total_questions = 20
    bill_problems = total_questions // 10
    ryan_problems = bill_problems * 2
    frank_problems = ryan_problems * 3
    problems_per_type = total_questions // 4
    
    type1 = frank_problems // problems_per_type
    remaining_problems = frank_problems % problems_per_type
    type2 = remaining_problems // (problems_per_type // 2)
    remaining_problems %= (problems_per_type // 2)
    type3 = remaining_problems // (problems_per_type // 4)
    type4 = remaining_problems % (problems_per_type // 4)
    
    result = (type1, type2, type3, type4)
    return result

print(solution())