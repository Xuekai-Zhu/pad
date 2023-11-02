def solution():
    # Define the number of pizzas ordered
    num_pizzas = 3

    # Define the number of toppings on each pizza
    toppings_per_pizza = {
        "pepperoni": 1,
        "sausage": 1,
        "black olive": 1,
        "mushroom": 1
    }

    # Calculate the total cost for the pizzas and toppings
    cost_per_pizza = 10 + sum(toppings_per_pizza.values())
    total_cost = num_pizzas * cost_per_pizza

    # Add the tip to the total cost
    total_cost += 5

    result = total_cost
    return result

print(solution())