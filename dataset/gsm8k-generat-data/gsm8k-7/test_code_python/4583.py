def solution():
    num_children = 2
    num_adults = 2
    cost_per_pizza = 10
    num_toppings = 2
    cost_per_topping = 1
    tip = 5

    # Calculate the total cost of pizzas for the children
    child_pizza_cost = num_children * (cost_per_pizza + (num_toppings * cost_per_topping))

    # Calculate the cost of the pizza split by the adults
    adult_pizza_cost = (cost_per_pizza + (num_toppings * cost_per_topping)) / 2

    # Calculate the total cost of the order
    total_cost = child_pizza_cost + adult_pizza_cost + tip
    result = total_cost
    return result

print(solution())