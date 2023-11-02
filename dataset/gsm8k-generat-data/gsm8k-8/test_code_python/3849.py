def solution():
    # Define the cost of lunch
    lunch_cost = 10

    # Define the cost of the ice cream cone
    ice_cream_cost = 5

    # Calculate the amount spent on the ice cream cone
    ice_cream_spending = ice_cream_cost / 0.25

    # Calculate the total amount spent
    total_spending = lunch_cost + ice_cream_spending

    # Calculate the amount of money Randy had at first
    initial_money = total_spending / 0.75

    result = initial_money
    return result

print(solution())