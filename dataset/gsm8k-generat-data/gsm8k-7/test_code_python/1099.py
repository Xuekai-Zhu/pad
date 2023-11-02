def solution():
    hot_dogs_per_hour = 10
    price_per_hot_dog = 2
    target_sales = 200

    # Calculate the number of hot dogs needed to reach the sales target
    num_hot_dogs_needed = target_sales / price_per_hot_dog

    # Calculate the number of hours needed to sell that many hot dogs
    num_hours_needed = num_hot_dogs_needed / hot_dogs_per_hour
    result = num_hours_needed
    return result

print(solution())