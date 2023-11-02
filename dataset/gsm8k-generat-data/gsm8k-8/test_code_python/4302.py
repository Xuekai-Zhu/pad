def solution():
    hot_dogs_per_day = 60
    pizzas_per_day = hot_dogs_per_day + 40

    # Assuming there are 30 days in June
    hot_dogs_in_June = hot_dogs_per_day * 30
    pizzas_in_June = pizzas_per_day * 30

    result = (hot_dogs_in_June, pizzas_in_June)
    return result

print(solution())