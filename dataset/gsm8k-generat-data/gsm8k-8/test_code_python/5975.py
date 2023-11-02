def solution():
    # Calculate the total weight of dog food needed per day for one dog
    dog_food_weight_per_day = 6 * 2 * 1/4  # 6 cups twice a day * 1/4 pound per cup

    # Calculate the total weight of dog food needed per day for two dogs
    total_dog_food_weight_per_day = dog_food_weight_per_day * 2

    # Calculate the total weight of dog food needed per month
    total_dog_food_weight_per_month = total_dog_food_weight_per_day * 30

    # Calculate the number of 20-pound bags needed
    num_bags = total_dog_food_weight_per_month / 20

    result = num_bags
    return result

print(solution())