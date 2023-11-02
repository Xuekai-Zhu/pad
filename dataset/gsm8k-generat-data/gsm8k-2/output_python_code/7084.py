def solution():
    """A school is planning a community outreach program. Each classroom must raise $200 for this activity. Classroom A has raised $20 from each of two families, $10 from each of eight families, and $5 from each of ten families. How much more money does Classroom A need in order to reach the goal?"""
    goal_money = 200
    raised_money = 0
    raised_money += 20 * 2  # $20 from each of two families
    raised_money += 10 * 8  # $10 from each of eight families
    raised_money += 5 * 10  # $5 from each of ten families
    remaining_money = goal_money - raised_money
    result = remaining_money
    return result

print(solution())