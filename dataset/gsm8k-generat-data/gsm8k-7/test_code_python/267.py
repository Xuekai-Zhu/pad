def solution():
    total_time_in_minutes = 7 * 60  # convert hours to minutes
    flour_weight = 22  # kg
    flour_per_pizza = 0.5  # kg
    time_per_pizza = 10  # minutes

    # Calculate the total time available in minutes
    total_time_available = total_time_in_minutes

    # Calculate the total flour used to make pizzas
    total_flour_used = (total_time_available / time_per_pizza) * flour_per_pizza

    # Calculate the remaining flour after making the pizzas
    remaining_flour = flour_weight - total_flour_used

    # Calculate the number of pizzas that can be made with the remaining flour
    remaining_pizzas = remaining_flour / flour_per_pizza
    result = remaining_pizzas
    return result

print(solution())