def solution():
    # Calculate the total weight of the dog food in grams
    total_weight = 2 * 50 * 1000  # 2 sacks of dog food, each weighing 50 kilograms

    # Calculate the total amount of food the dogs can consume in one day
    total_food_per_day = 4 * 250 * 2  # four dogs, fed twice a day, each consuming 250 grams of food per meal

    # Calculate the number of days the dog food will last
    days_last = total_weight / total_food_per_day
    result = days_last
    return result

print(solution())