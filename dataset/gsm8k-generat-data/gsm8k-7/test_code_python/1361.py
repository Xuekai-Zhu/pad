def solution():
    hamburgers = 8
    hamburger_price = 4
    milkshakes = 6
    milkshake_price = 5
    remaining_money = 70

    # Calculate the total amount of money spent on hamburgers
    hamburgers_cost = hamburgers * hamburger_price

    # Calculate the total amount of money spent on milkshakes
    milkshakes_cost = milkshakes * milkshake_price

    # Calculate the total amount of money spent on food
    total_cost = hamburgers_cost + milkshakes_cost

    # Calculate the amount of money Annie had at first
    initial_money = total_cost + remaining_money
    result = initial_money
    return result

print(solution())