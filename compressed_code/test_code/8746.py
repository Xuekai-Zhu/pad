def solution():
    
    num_disco_balls = 4
    num_food_boxes = 10
    budget = 330
    cost_per_food_box = 25
    total_food_cost = num_food_boxes * cost_per_food_box
    total_disco_ball_cost = budget - total_food_cost
    cost_per_disco_ball = total_disco_ball_cost / num_disco_balls
    result = cost_per_disco_ball
    return result

print(solution())