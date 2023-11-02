def solution():
    # Calculate the total cost of the food boxes
    food_cost = 10 * 25

    # Subtract the food cost from the total budget to get the budget for the disco balls
    disco_ball_budget = 330 - food_cost

    # Divide the disco ball budget by the number of disco balls to get the cost per ball
    cost_per_ball = disco_ball_budget / 4

    result = cost_per_ball
    return result

print(solution())