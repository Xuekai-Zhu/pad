def solution():
    """Jake can wash his car with 1 bottle of car wash soap 4 times. If each bottle costs $4.00, and he washes his car once a week for 20 weeks, how much does he spend on car soap?"""
    bottles_per_use = 1 / 4
    cost_per_bottle = 4
    uses_per_week = 1
    weeks = 20
    total_uses = uses_per_week * weeks
    total_bottles = total_uses / bottles_per_use
    total_cost = total_bottles * cost_per_bottle
    result = total_cost
    return result

print(solution())