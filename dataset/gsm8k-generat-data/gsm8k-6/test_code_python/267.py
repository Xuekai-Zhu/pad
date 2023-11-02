def solution():
    # Calculate the total time Jimmy has to make pizzas in minutes
    total_time = 7 * 60

    # Calculate the number of pizzas Jimmy can make with the given amount of flour
    flour_weight = 22  # kilograms
    flour_per_pizza = 0.5  # kilograms
    max_pizzas = (flour_weight / flour_per_pizza)
    time_per_pizza = 10  # minutes
    total_pizzas = min(max_pizzas, total_time/time_per_pizza)

    # Calculate the amount of flour left after making the pizzas
    flour_left = flour_weight - (total_pizzas * flour_per_pizza)

    result = int(total_pizzas)
    return result

print(solution())