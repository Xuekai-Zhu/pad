def solution():
    """For 6 weeks in the summer, Erica treats herself to 1 ice cream cone from the ice cream truck. Monday, Wednesday and Friday she gets a $2.00 orange creamsicle. Tuesday and Thursday she gets a $1.50 ice cream sandwich. Saturday and Sunday she gets a $3.00 Nutty-Buddy. How much money does she spend on ice cream in 6 weeks?"""
    total_weeks = 6
    total_cost = (3 * 2 + 2 * 1.5 + 2 * 3) * total_weeks
    result = total_cost
    return result

print(solution())