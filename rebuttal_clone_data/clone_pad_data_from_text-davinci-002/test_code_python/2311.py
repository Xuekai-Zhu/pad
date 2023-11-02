def solution():
    dogs = 3
    food_per_dog_per_day = .5
    days_in_week = 7
    total_food = 30
    food_eaten = dogs * food_per_dog_per_day * 2 * days_in_week
    food_left = total_food - food_eaten
    result = food_left
    
    return result

print(solution())