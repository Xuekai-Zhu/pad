def solution():
    """Oliver had $9, then he saved $5 from his allowance and spent $4 on a frisbee and $3 on a puzzle. His friend gives him another $8 as it's his birthday. How much money does Oliver have left?"""
    starting_money = 9
    allowance = 5
    frisbee_cost = 4
    puzzle_cost = 3
    birthday_money = 8
    total_spent = frisbee_cost + puzzle_cost
    total_money = starting_money + allowance + birthday_money - total_spent
    result = total_money
    return result

print(solution())