def solution():
     special_food_needed_per_day = 2
     days_special_food_needed = 60
     total_special_food_needed = special_food_needed_per_day * days_special_food_needed
     
     regular_food_needed_per_day = 4
     days_regular_food_needed = 365 - days_special_food_needed
     total_regular_food_needed = regular_food_needed_per_day * days_regular_food_needed
     
     total_food_needed = total_special_food_needed + total_regular_food_needed
     
     size_of_bag = 5
     pounds_in_bag = 16
     ounces_in_pound = 16
     ounces_in_bag = size_of_bag * pounds_in_bag * ounces_in_pound
     bags_needed = total_food_needed / ounces_in_bag
     result = bags_needed
     
     return result

print(solution())