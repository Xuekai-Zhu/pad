def solution():
    # Define the time and flour constraints
    total_time = 420 # 7 hours * 60 minutes
    flour = 22

    # Calculate the maximum number of pizzas he can make
    max_pizzas = flour / 0.5

    # Calculate the total time it takes to make all the pizzas
    total_pizza_time = max_pizzas * 10

    # Calculate the remaining time after making all the pizzas
    remaining_time = total_time - total_pizza_time

    # Calculate the number of pizzas he can make with the remaining flour in the remaining time
    extra_pizzas = (flour - (max_pizzas * 0.5)) / 0.5

    # Calculate the total number of pizzas he can bring home
    total_pizzas = max_pizzas + extra_pizzas

    result = total_pizzas
    return result

print(solution())