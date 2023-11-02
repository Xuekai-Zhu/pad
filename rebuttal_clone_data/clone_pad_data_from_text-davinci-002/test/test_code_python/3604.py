def solution():
     total_balls = 100
     balls_with_holes = total_balls * 0.40
     balls_left = total_balls - balls_with_holes
     balls_exploded = balls_left * 0.20
     balls_inflated = balls_left - balls_exploded
     result = balls_inflated
     return result

print(solution())