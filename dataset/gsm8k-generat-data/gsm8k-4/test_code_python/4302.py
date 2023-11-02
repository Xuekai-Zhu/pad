def solution():
    """A restaurant makes 40 more pizzas than hot dogs every day. If the restaurant makes 60 hot dogs every day, how many pizzas and hot dogs will it make in June?"""
    # Define the number of hot dogs made each day
    hot_dogs_per_day = 60

    # Calculate the number of pizzas made each day
    pizzas_per_day = hot_dogs_per_day + 40

    # Calculate the total number of pizzas and hot dogs made in June
    total_hot_dogs = hot_dogs_per_day * 30
    total_pizzas = pizzas_per_day * 30

    # return the result
    result = f"The restaurant will make {total_hot_dogs} hot dogs and {total_pizzas} pizzas in June."
    return result

print(solution())