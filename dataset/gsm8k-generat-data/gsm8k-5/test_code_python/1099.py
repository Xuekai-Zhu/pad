def solution():
    hot_dogs_per_hour = 10  # The stand sells 10 hot dogs every hour
    price_per_hot_dog = 2  # Each hot dog sells for $2
    target_sales = 200  # The stand wants to make $200 in sales

    # Calculate the number of hours the stand needs to run to make $200 in sales
    hours_needed = target_sales / (hot_dogs_per_hour * price_per_hot_dog)
    result = hours_needed
    return result

print(solution())