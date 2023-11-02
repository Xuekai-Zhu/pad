def solution():
    """Jimmy is going to sell pizzas at the carnival to make some money. The carnival only gave him 7 hours to do so. He bought a 22kg sack of flour to make his pizzas and he takes 10 min to make each pizza for the customers. At the end of the 7 hours, he saw some flour was left. Knowing that each pizza needs 0.5kg of flour to make, how many pizzas can he make to bring home with the flour left?"""
    total_time = 7*60  # converting hours to minutes
    flour_weight = 22
    pizza_flour_weight = 0.5
    pizza_time = 10
    total_pizza_time = (flour_weight // pizza_flour_weight) * pizza_time
    remaining_time = total_time - total_pizza_time
    pizzas = remaining_time // pizza_time
    result = pizzas
    return result

print(solution())