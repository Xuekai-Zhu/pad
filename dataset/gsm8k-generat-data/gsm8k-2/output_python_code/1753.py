def solution():
    """Emma got $2000 from the bank. She bought $400 of furniture and gave 3/4 of the rest to her friend Anna. How much is left with Emma?"""
    starting_money = 2000
    furniture_cost = 400
    remaining_money = starting_money - furniture_cost
    anna_share = 0.75 * remaining_money
    emma_remaining = remaining_money - anna_share
    result = emma_remaining
    return result

print(solution())