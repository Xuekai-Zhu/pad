def solution():
    num_cups_lemonade = 2
    cost_cup_lemonade = 2

    num_sandwiches = 2
    cost_sandwich = 2.5

    total_cost = (num_cups_lemonade * cost_cup_lemonade) + (num_sandwiches * cost_sandwich)
    amount_paid = 20

    change = amount_paid - total_cost
    result = change
    return result

print(solution())