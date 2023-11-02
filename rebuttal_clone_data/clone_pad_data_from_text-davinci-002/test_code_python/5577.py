def solution():
     ounces_in_large_barrel = 35
     ounces_in_small_barrel = 24
     servings_in_small_barrel = 60
     balls_per_serving = 12
     total_balls_in_small_barrel = servings_in_small_barrel * balls_per_serving
     total_balls_in_large_barrel = ounces_in_large_barrel / ounces_in_small_barrel * total_balls_in_small_barrel
     result = total_balls_in_large_barrel
     return result

print(solution())