def solution():
    """Jimmy is going to sell pizzas at the carnival to make some money. The carnival only gave him 7 hours to do so. He bought a 22kg sack of flour to make his pizzas and he takes 10 min to make each pizza for the customers. At the end of the 7 hours, he saw some flour was left. Knowing that each pizza needs 0.5kg of flour to make, how many pizzas can he make to bring home with the flour left?"""
    # Define the amount of flour Jimmy purchased
    flour = 22

    # Convert the time given into minutes
    time = 7 * 60

    # Calculate the number of pizzas Jimmy can make
    pizzas = (flour // 0.5)  # Round down to the nearest whole number of pizzas
    max_pizzas = time // 10  # Limit the number of pizzas he can make by the time available
    actual_pizzas = min(pizzas, max_pizzas)  # Take the smaller of the two values

    # Calculate the amount of flour left after making pizzas
    flour_left = flour - actual_pizzas * 0.5

    # Display the number of pizzas Jimmy can make and the amount of flour left
    result = {"pizzas": actual_pizzas, "flour_left": flour_left}
    return result

print(solution())