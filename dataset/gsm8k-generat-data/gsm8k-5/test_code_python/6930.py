def solution():
    starting_money = 9  # Josh starts with 9 dollars
    drink_cost = 1.75  # Josh spends 1.75 dollars on a drink
    second_purchase = 1.25  # Josh spends 1.25 dollars on another purchase

    # Calculate how much money Josh has left
    remaining_money = starting_money - drink_cost - second_purchase
    result = remaining_money
    return result

print(solution())