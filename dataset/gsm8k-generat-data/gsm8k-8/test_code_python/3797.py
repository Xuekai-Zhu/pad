def solution():
    # Define Ivan's starting money
    initial_money = 10

    # Calculate how much money Ivan spent on cupcakes
    cupcakes_cost = initial_money * (1/5)

    # Calculate how much money Ivan had left after buying cupcakes
    money_after_cupcakes = initial_money - cupcakes_cost

    # Calculate how much money Ivan spent on the milkshake
    milkshake_cost = money_after_cupcakes - 3

    result = milkshake_cost
    return result

print(solution())