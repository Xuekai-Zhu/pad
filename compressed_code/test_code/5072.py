def solution():
    
    dogs = 4
    meals_per_day = 2
    food_per_meal = 250/1000  
    total_food_per_day = dogs * meals_per_day * food_per_meal
    total_food = 2 * 50  
    days = total_food / total_food_per_day
    result = days
    return result

print(solution())