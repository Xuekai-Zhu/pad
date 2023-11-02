def solution():
    # Calculate the total amount of food needed for all the horses in a day
    food_per_day = 25 * 2 * 20  # 25 horses, fed twice a day, with 20 pounds of food each time = 1000 pounds of food per day
    food_per_bag = 1000 / 2000  # each bag contains half a ton, which is 1000 pounds

    # Calculate the number of bags needed for 60 days
    bags_per_day = food_per_day / 1000
    bags_needed = bags_per_day * 60

    result = bags_needed
    return result

print(solution())