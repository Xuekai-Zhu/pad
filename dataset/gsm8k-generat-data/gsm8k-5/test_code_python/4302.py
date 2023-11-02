def solution():
    hot_dogs_per_day = 60  # The restaurant makes 60 hot dogs per day
    pizzas_per_day = hot_dogs_per_day + 40  # The restaurant makes 40 more pizzas than hot dogs per day
    days_in_june = 30  # There are 30 days in June

    # Calculate the total number of hot dogs and pizzas made in June
    total_hot_dogs = hot_dogs_per_day * days_in_june
    total_pizzas = pizzas_per_day * days_in_june
    result = (total_hot_dogs, total_pizzas)
    return result

print(solution())