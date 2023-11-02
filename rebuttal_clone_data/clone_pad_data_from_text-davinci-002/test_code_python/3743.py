def solution():
     disco_balls = 4
     boxes_of_food = 10
     food_cost = 25
     total_cost = 330
     disco_ball_cost = (total_cost - (boxes_of_food * food_cost)) / disco_balls
     result = disco_ball_cost
     return result

print(solution())