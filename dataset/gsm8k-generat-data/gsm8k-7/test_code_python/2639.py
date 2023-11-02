def solution():
    total_money = 75
    ticket_cost = 30
    food_cost = 13
    tshirt_cost = 23

    # Calculate the total amount spent by Mitzi
    total_spent = ticket_cost + food_cost + tshirt_cost

    # Calculate the amount of money that Mitzi has left
    money_left = total_money - total_spent
    result = money_left
    return result

print(solution())