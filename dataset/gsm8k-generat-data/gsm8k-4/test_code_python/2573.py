def solution():
    """Bill composes 20 total math questions for money.  Ryan composes twice as many problems as Bill, and Frank composes 3 times as many as Ryan.  
    Assuming each person has to compose 4 different types of math problems in equal proportion out of the total amount, how many problems of each type does Frank compose?"""
    
    # Define the total number of math problems
    total_problems = 20

    # Define the number of problems that Bill composes
    bill_problems = total_problems / 6 # 6 types of problems total

    # Define the number of problems that Ryan composes
    ryan_problems = bill_problems * 2

    # Define the number of problems that Frank composes
    frank_problems = ryan_problems * 3

    # Define the number of problems per type for each person
    problems_per_type = frank_problems / 4

    # return the result
    result = problems_per_type
    return result

print(solution())