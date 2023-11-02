def solution():
    uses_per_bottle = 4
    cost_per_bottle = 4.0
    num_weeks = 20
    uses_per_week = 1

    # Calculate the total number of times Jake will use car wash soap
    total_uses = num_weeks * uses_per_week

    # Calculate the total number of bottles of car wash soap Jake will need
    total_bottles = total_uses / uses_per_bottle

    # Calculate the total cost of all bottles of car wash soap Jake will buy
    total_cost = total_bottles * cost_per_bottle
    result = total_cost
    return result

print(solution())