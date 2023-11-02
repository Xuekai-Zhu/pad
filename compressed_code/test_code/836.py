def solution():
    
    hot_dogs_per_hour = 10
    price_per_hot_dog = 2
    total_sales_needed = 200
    hot_dogs_needed = total_sales_needed / price_per_hot_dog
    hours_needed = hot_dogs_needed / hot_dogs_per_hour
    result = hours_needed
    return result

print(solution())