def solution():
    
    puppy_cost = 10
    food_per_day = 1/3
    weeks_of_food = 3
    cups_per_bag = 3.5
    bag_cost = 2
    total_food_cups = food_per_day * 7 * weeks_of_food
    total_bags = total_food_cups / cups_per_bag
    total_food_cost = total_bags * bag_cost
    total_cost = puppy_cost + total_food_cost
    result = total_cost
    return result

print(solution())