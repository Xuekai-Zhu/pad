def solution():
    total_time = 7*60  # Jimmy has 7 hours to sell pizzas, converted to minutes
    flour_weight = 22  # Jimmy has a 22kg sack of flour
    pizza_flour_weight = 0.5  # Each pizza needs 0.5kg of flour
    time_per_pizza = 10  # Jimmy takes 10 min to make each pizza

    # Calculate the number of pizzas Jimmy can make based on the flour he has
    num_pizzas = flour_weight // pizza_flour_weight

    # Calculate the total time it would take Jimmy to make that many pizzas
    total_pizza_time = num_pizzas * time_per_pizza

    # Calculate the time Jimmy has left to sell pizzas
    remaining_time = total_time - total_pizza_time

    # Calculate the additional pizzas Jimmy can make with the remaining flour and time
    additional_pizzas = remaining_time // time_per_pizza

    # Calculate the total number of pizzas Jimmy can make
    total_pizzas = num_pizzas + additional_pizzas
    result = total_pizzas
    return result

print(solution())