def solution():
    """Thirty students run in a charity race to raise money for the hurricane victims. Ten of the students raised $20 each. The rest of the students raised $30 each. How much did the students raise in all?"""
    num_students_raising_20 = 10
    num_students_raising_30 = 20
    money_raised_by_students_raising_20 = num_students_raising_20 * 20
    money_raised_by_students_raising_30 = num_students_raising_30 * 30
    total_money_raised = money_raised_by_students_raising_20 + money_raised_by_students_raising_30
    result = total_money_raised
    return result

print(solution())