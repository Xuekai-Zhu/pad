def solution():
    ball_cost = 3.75  # Cost of the football
    shorts_cost = 2.4  # Cost of the shorts
    shoes_cost = 11.85  # Cost of the football shoes
    budget = 10  # Zachary has $10

    # Calculate the total cost of the items
    total_cost = ball_cost + shorts_cost + shoes_cost

    # Calculate the amount of money Zachary still needs
    remaining_money = total_cost - budget
    result = remaining_money
    return result

print(solution())