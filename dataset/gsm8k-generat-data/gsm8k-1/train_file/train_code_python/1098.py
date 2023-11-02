def solution():
    """A hot dog stand sells 10 hot dogs every hour, each one selling for $2. How many hours does the stand need to run to make $200 in sales?"""
    hot_dogs_per_hour = 10
    price_per_hot_dog = 2
    target_sales = 200
    hours_needed = target_sales / (hot_dogs_per_hour * price_per_hot_dog)
    result = hours_needed
    return result

print(solution())