def solution():
    """Calum runs a nightclub and decides to run a disco night to attract different customers. He is planning the event and is calculating how much he can spend on each item without spending more than he has budgeted. He only needs to buy 4 disco balls and 10 boxes of food. Each box of food costs $25. Calum’s budget for the disco balls and food is $330. How much, in dollars, can Calum afford to spend on each disco ball?"""
    num_disco_balls = 4
    num_food_boxes = 10
    food_cost_per_box = 25
    total_budget = 330
    total_food_cost = num_food_boxes * food_cost_per_box
    max_disco_ball_cost = (total_budget - total_food_cost) / num_disco_balls
    result = max_disco_ball_cost
    return result

print(solution())