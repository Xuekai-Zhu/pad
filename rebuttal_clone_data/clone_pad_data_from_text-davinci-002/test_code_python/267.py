def solution():
    """Jimmy is going to sell pizzas at the carnival to make some money. The carnival only gave him 7 hours to do so. He bought a 22kg sack of flour to make his pizzas and he takes 10 min to make each pizza for the customers. At the end of the 7 hours, he saw some flour was left. Knowing that each pizza needs 0.5kg of flour to make, how many pizzas can he make to bring home with the flour left?"""
    hours_available = 7
    minutes_to_make_pizza = 10
    flour_needed_per_pizza = 0.5
    total_flour_available = 22
    pizzas_made = (hours_available * 60 - minutes_to_make_pizza) / minutes_to_make_pizza
    flour_left = total_flour_available - pizzas_made * flour_needed_per_pizza
    result = pizzas_made
    return result

print(solution())