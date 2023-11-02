def solution():
    # Calculate how much Ivan spent on cupcakes and how much he had left
    initial_money = 10  # Ivan had $10 initially
    cupcakes_cost = initial_money * (1/5)  # Ivan spent 1/5 of his money on cupcakes
    remaining_money = initial_money - cupcakes_cost  # Ivan had this much money left after buying cupcakes
    milkshake_cost = remaining_money - 3  # Ivan spent some money on a milkshake and had $3 left

    result = milkshake_cost
    return result

print(solution())