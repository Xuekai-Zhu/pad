def solution():
    num_disco_balls = 4  # Calum only needs 4 disco balls
    num_boxes_of_food = 10  # Calum needs 10 boxes of food
    budget = 330  # Calum has a budget of $330

    # Calculate the total cost of the food
    food_cost = num_boxes_of_food * 25  # Each box of food costs $25

    # Calculate the maximum amount Calum can spend on the disco balls
    max_disco_ball_cost = (budget - food_cost) / num_disco_balls

    result = max_disco_ball_cost
    return result

print(solution())