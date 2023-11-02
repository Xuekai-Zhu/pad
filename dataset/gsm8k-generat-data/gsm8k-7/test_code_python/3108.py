def solution():
    annie_money = 120
    hamburger_price = 4
    milkshake_price = 3
    num_hamburgers = 8
    num_milkshakes = 6

    # Calculate the total cost of hamburgers
    hamburger_cost = hamburger_price * num_hamburgers

    # Calculate the total cost of milkshakes
    milkshake_cost = milkshake_price * num_milkshakes

    # Calculate the total cost of all items
    total_cost = hamburger_cost + milkshake_cost

    # Calculate the amount of money Annie has left
    money_left = annie_money - total_cost
    result = money_left
    return result

print(solution())