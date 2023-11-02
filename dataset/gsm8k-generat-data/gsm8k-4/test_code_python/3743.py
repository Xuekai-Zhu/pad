def solution():
    """Calum runs a nightclub and decides to run a disco night to attract different customers. He is planning the event and is calculating how much he can spend on each item without spending more than he has budgeted. He only needs to buy 4 disco balls and 10 boxes of food. Each box of food costs $25. Calum’s budget for the disco balls and food is $330. How much, in dollars, can Calum afford to spend on each disco ball?"""
    # Define the number of disco balls and boxes of food
    disco_balls = 4
    food_boxes = 10

    # Define the total budget
    budget = 330

    # Calculate the total cost of the food
    food_cost = food_boxes * 25

    # Calculate the maximum amount that can be spent on the disco balls
    disco_ball_budget = budget - food_cost

    # Calculate the maximum amount that can be spent on each disco ball
    disco_ball_price = disco_ball_budget / disco_balls

    # return the result
    result = disco_ball_price
    return result

print(solution())