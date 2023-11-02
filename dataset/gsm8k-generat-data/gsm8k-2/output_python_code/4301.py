def solution():
    """A restaurant makes 40 more pizzas than hot dogs every day. If the restaurant makes 60 hot dogs every day, how many pizzas and hot dogs will it make in June?"""
    hot_dogs_per_day = 60
    pizzas_per_day = hot_dogs_per_day + 40
    total_days_in_June = 30
    total_hot_dogs_in_June = hot_dogs_per_day * total_days_in_June
    total_pizzas_in_June = pizzas_per_day * total_days_in_June
    result = (total_hot_dogs_in_June, total_pizzas_in_June)
    return result

print(solution())