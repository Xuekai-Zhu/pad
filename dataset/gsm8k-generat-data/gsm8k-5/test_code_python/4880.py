def solution():
    # Calculate the total cost of their meal
    cheeseburger_price = 3
    milkshake_price = 5
    cheese_fries_price = 8

    total_cost = (2 * cheeseburger_price) + (2 * milkshake_price) + cheese_fries_price

    # Calculate the amount of money spent by Jim
    jim_spent = 0.8 * 20

    # Calculate the amount of money spent by Jim's cousin
    cousin_spent = total_cost - jim_spent

    result = cousin_spent
    return result

print(solution())