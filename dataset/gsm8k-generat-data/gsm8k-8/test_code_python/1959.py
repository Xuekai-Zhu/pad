def solution():
    # Define the starting amount of money and the amount spent
    starting_amount = 11
    amount_spent = 2

    # Calculate how much money is left after the spending
    money_left = 3

    # Calculate how much money Abigail had before she lost some
    previous_amount = starting_amount - amount_spent

    # Calculate how much money Abigail has lost
    lost_money = previous_amount - money_left
    result = lost_money
    return result

print(solution())