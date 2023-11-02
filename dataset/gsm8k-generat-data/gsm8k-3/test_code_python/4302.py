def solution():
    """A restaurant makes 40 more pizzas than hot dogs every day. If the restaurant makes 60 hot dogs every day, how many pizzas and hot dogs will it make in June?"""
    # Define the number of hot dogs made each day
    hot_dogs = 60

    # Calculate the number of pizzas made each day
    pizzas = hot_dogs + 40

    # Calculate the total number of hot dogs and pizzas made in June (30 days)
    total_hot_dogs = hot_dogs * 30
    total_pizzas = pizzas * 30

    # Display the total number of hot dogs and pizzas made in June
    result = (total_hot_dogs, total_pizzas)
    return result

print(solution())