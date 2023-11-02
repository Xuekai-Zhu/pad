def solution():
    """Jimmy is going to sell pizzas at the carnival to make some money. The carnival only gave him 7 hours to do so. He bought a 22kg sack of flour to make his pizzas and he takes 10 min to make each pizza for the customers. At the end of the 7 hours, he saw some flour was left. Knowing that each pizza needs 0.5kg of flour to make, how many pizzas can he make to bring home with the flour left?"""
    total_time = 7 * 60  # convert 7 hours to minutes
    flour = 22  # kg
    flour_per_pizza = 0.5  # kg
    time_per_pizza = 10  # minutes
    max_pizzas = flour // flour_per_pizza  # calculate maximum number of pizzas he can make
    max_time = max_pizzas * time_per_pizza  # calculate maximum time it would take to make all the pizzas
    leftover_flour = flour - (max_pizzas * flour_per_pizza)  # calculate leftover flour
    if max_time > total_time:  # if he doesn't have enough time to make all the pizzas
        num_pizzas = (total_time // time_per_pizza)  # calculate number of pizzas he can make in the given time
    else:
        num_pizzas = max_pizzas  # otherwise, he can make all the pizzas with the given flour
    result = num_pizzas
    return result

print(solution())