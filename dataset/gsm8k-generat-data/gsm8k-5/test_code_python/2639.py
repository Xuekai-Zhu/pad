def solution():
    initial_amount = 75  # Mitzi brought $75 to the amusement park
    ticket_cost = 30  # Mitzi spent $30 on a ticket
    food_cost = 13  # Mitzi spent $13 on food
    tshirt_cost = 23  # Mitzi spent $23 on a T-shirt

    # Calculate the total amount Mitzi spent
    total_spent = ticket_cost + food_cost + tshirt_cost

    # Calculate the amount of money Mitzi has left
    money_left = initial_amount - total_spent
    result = money_left
    return result

print(solution())