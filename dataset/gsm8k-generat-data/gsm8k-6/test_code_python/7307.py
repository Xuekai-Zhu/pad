def solution():
    # Calculate the cost of the puppy, food per day, and food per week
    puppy_cost = 10
    food_per_day = 1/3
    food_per_week = food_per_day * 7 * 3.5 / 3
    food_cost = food_per_week * 2 * 3  # 3 weeks of food
    total_cost = puppy_cost + food_cost
    result = total_cost
    return result

print(solution())