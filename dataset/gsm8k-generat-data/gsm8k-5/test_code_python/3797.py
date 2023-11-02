def solution():
    starting_money = 10  # Ivan started with $10
    cupcakes_cost = starting_money / 5  # Ivan spent 1/5 of his money on cupcakes
    remaining_money = starting_money - cupcakes_cost  # Ivan has this much money left after buying cupcakes
    left_money = 3  # Ivan had $3 left after buying a milkshake

    # Calculate the cost of the milkshake
    milkshake_cost = remaining_money - left_money
    result = milkshake_cost
    return result

print(solution())