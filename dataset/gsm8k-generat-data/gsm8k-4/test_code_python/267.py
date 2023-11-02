def solution():
    """Jimmy is going to sell pizzas at the carnival to make some money. The carnival only gave him 7 hours to do so. He bought a 22kg sack of flour to make his pizzas and he takes 10 min to make each pizza for the customers. At the end of the 7 hours, he saw some flour was left. Knowing that each pizza needs 0.5kg of flour to make, how many pizzas can he make to bring home with the flour left?"""
    # Define the sack of flour in kg
    flour = 22

    # Define the time available to Jimmy in minutes
    time_available = 7 * 60

    # Define the time needed to make one pizza in minutes
    time_per_pizza = 10

    # Define the amount of flour needed to make one pizza in kg
    flour_per_pizza = 0.5

    # Calculate the total number of pizzas that can be made
    total_pizzas = flour // flour_per_pizza

    # Calculate the total time needed to make all the pizzas
    total_time = total_pizzas * time_per_pizza

    # Calculate the time left after making all the pizzas
    time_left = time_available - total_time

    # Calculate the number of additional pizzas that can be made with the remaining flour
    additional_pizzas = (flour % flour_per_pizza) * 2

    # Calculate the final total number of pizzas that can be made
    final_total_pizzas = total_pizzas + additional_pizzas

    # Display the number of pizzas that can be made with the remaining flour
    result = final_total_pizzas
    return result

print(solution())