def solution():
    """Calum runs a nightclub and decides to run a disco night to attract different customers. He is planning the event and is calculating how much he can spend on each item without spending more than he has budgeted. He only needs to buy 4 disco balls and 10 boxes of food. Each box of food costs $25. Calum’s budget for the disco balls and food is $330. How much, in dollars, can Calum afford to spend on each disco ball?"""
    # Define the number of disco balls and boxes of food needed
    DISCO_BALLS = 4
    FOOD_BOXES = 10

    # Define the cost of each box of food
    FOOD_COST = 25

    # Define Calum's budget for the disco balls and food
    BUDGET = 330

    # Calculate the total cost of the food
    total_food_cost = FOOD_BOXES * FOOD_COST

    # Calculate the maximum amount Calum can spend on each disco ball
    max_disco_ball_cost = (BUDGET - total_food_cost) / DISCO_BALLS

    # Display the maximum cost per disco ball
    result = max_disco_ball_cost
    return result

print(solution())