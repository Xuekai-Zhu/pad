def solution():
    hot_dogs_per_hour = 10
    price_per_hot_dog = 2
    desired_sales = 200
    hours_needed = desired_sales / (hot_dogs_per_hour * price_per_hot_dog)
    result = hours_needed
    return result

print(solution())