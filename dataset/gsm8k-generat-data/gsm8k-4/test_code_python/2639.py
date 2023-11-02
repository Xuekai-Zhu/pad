def solution():
    """Mitzi brought $75 to the amusement park. She spent $30 on a ticket, $13 on food, and $23 on a T-shirt. How much money does she have left?"""
    # Define the initial amount of money Mitzi had
    initial_money = 75

    # Define the amount of money Mitzi spent
    total_spent = 30 + 13 + 23

    # Calculate the amount of money Mitzi has left
    money_left = initial_money - total_spent

    # Return the result
    result = money_left
    return result

print(solution())