def solution():
    # Define the number of disco balls and boxes of food
    num_disco_balls = 4
    num_food_boxes = 10

    # Define the total cost of the food boxes
    total_food_cost = num_food_boxes * 25

    # Define the remaining budget for the disco balls
    disco_ball_budget = 330 - total_food_cost

    # Calculate the cost per disco ball
    cost_per_disco_ball = disco_ball_budget / num_disco_balls

    result = cost_per_disco_ball
    return result

print(solution())