def solution():
    # Calculate the cost of the drinks
    drinks_cost = 6 * 6

    # Calculate the total cost before tip
    total_cost = 20 + drinks_cost + 14

    # Calculate the cost of the tip
    tip = 0.3 * total_cost

    # Calculate the total cost after tip
    total_cost = total_cost + tip

    # Calculate the cost of the 2 rounds of drinks for his friends
    friends_drinks_cost = 2 * 6 * 5

    # Add the cost of the friends' drinks to the total cost
    total_cost = total_cost + friends_drinks_cost

    result = round(total_cost, 2)
    return result

print(solution())