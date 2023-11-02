def solution():
    dogs = [20, 40, 10, 30, 50]  # Weight of each dog in pounds
    food_per_pound = 1/10  # Each pound of dog needs 1/10 pound of dog food
    total_food_per_day = sum(dogs) * food_per_pound  # Total amount of dog food needed per day
    result = total_food_per_day
    return result

print(solution())