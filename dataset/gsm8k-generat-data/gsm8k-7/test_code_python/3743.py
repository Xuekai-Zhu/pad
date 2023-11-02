def solution():
    num_disco_balls = 4
    num_food_boxes = 10
    food_box_cost = 25
    total_budget = 330

    # Calculate the total cost of all food boxes
    total_food_cost = num_food_boxes * food_box_cost

    # Calculate the remaining budget for the disco balls
    disco_ball_budget = total_budget - total_food_cost

    # Calculate the cost of each disco ball
    disco_ball_cost = disco_ball_budget / num_disco_balls
    result = disco_ball_cost
    return result

print(solution())