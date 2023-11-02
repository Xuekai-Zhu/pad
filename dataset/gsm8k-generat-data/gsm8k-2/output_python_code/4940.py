def solution():
    """Thirty students run in a charity race to raise money for the hurricane victims. Ten of the students raised $20 each. The rest of the students raised $30 each. How much did the students raise in all?"""
    num_students = 30
    num_20_dollar = 10
    num_30_dollar = num_students - num_20_dollar
    total_raised = (num_20_dollar * 20) + (num_30_dollar * 30)
    result = total_raised
    return result

print(solution())