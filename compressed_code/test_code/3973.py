def solution():
    
    dog_weights = [20, 40, 10, 30, 50]
    total_weight = sum(dog_weights)
    food_per_day = total_weight / 10
    result = food_per_day
    return result

print(solution())