def solution():
    """A hot dog stand sells 10 hot dogs every hour, each one selling for $2. How many hours does the stand need to run to make $200 in sales?"""
    hot_dogs_per_hour = 10
    price_per_hot_dog = 2
    total_sales_needed = 200
    hot_dogs_needed = total_sales_needed / price_per_hot_dog
    hours_needed = hot_dogs_needed / hot_dogs_per_hour
    result = hours_needed
    return result

print(solution())