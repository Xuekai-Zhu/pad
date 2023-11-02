def solution():
    puppy_cost = 10
    food_per_day = 1/3
    bag_size = 3.5
    bag_cost = 2
    num_weeks = 3

    # Calculate the total cost of food for the puppy
    total_food = (food_per_day * 7) * num_weeks
    num_bags = total_food / bag_size
    total_food_cost = num_bags * bag_cost

    # Calculate the total cost of the puppy and food
    total_cost = puppy_cost + total_food_cost
    result = total_cost
    return result

print(solution())