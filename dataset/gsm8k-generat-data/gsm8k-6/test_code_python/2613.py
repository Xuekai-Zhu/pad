def solution():
    # Calculate total amount spent on beef
    beef_cost = 5 * x  # Assume Tony bought x pounds of beef

    # Calculate total amount spent on cheese
    cheese_cost = 7 * y  # Assume Tony bought y pounds of cheese

    # Calculate total amount spent
    total_spent = beef_cost + cheese_cost

    # Calculate how much money Tony has left
    remaining_money = 87 - total_spent

    # Calculate how much money Tony had before buying cheese
    money_before_cheese = remaining_money + 61

    # Calculate how many pounds of cheese he bought
    cheese_pounds = money_before_cheese / 7
    result = cheese_pounds
    return result

print(solution())