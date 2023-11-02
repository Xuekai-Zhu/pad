def solution():
     lollipops = 100
     hard_candies = 5
     lollipop_food_coloring = 5
     total_food_coloring = 600
     hard_candy_food_coloring = (total_food_coloring - (lollipops * lollipop_food_coloring)) / hard_candies
     result = hard_candy_food_coloring
     return result

print(solution())