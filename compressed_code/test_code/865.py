def solution():
    
    dogs = 4
    food_per_dog_per_day = 250
    days_on_vacation = 14
    total_food_needed = dogs * food_per_dog_per_day * days_on_vacation / 1000
    result = total_food_needed
    return result

print(solution())