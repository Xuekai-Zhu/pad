def solution():
    
    num_disco_balls = 4
    num_food_boxes = 10
    food_cost_per_box = 25
    total_budget = 330
    total_food_cost = num_food_boxes * food_cost_per_box
    max_disco_ball_cost = (total_budget - total_food_cost) / num_disco_balls
    result = max_disco_ball_cost
    return result

print(solution())