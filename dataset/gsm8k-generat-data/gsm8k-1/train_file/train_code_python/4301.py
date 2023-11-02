def solution():
    """A restaurant makes 40 more pizzas than hot dogs every day. If the restaurant makes 60 hot dogs every day, how many pizzas and hot dogs will it make in June?"""
    hot_dogs_per_day = 60
    pizzas_per_day = hot_dogs_per_day + 40
    days_in_June = 30
    total_hot_dogs = hot_dogs_per_day * days_in_June
    total_pizzas = pizzas_per_day * days_in_June
    result = (total_hot_dogs, total_pizzas)
    return result

print(solution())