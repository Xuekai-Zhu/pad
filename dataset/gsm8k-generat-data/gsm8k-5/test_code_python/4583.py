def solution():
    # Quantity of pizza ordered
    pizza_ordered = 2  # Ruby ordered 2 pizzas for her children and 1 to share with her husband

    # Total toppings ordered
    toppings_ordered = 5  # Pepperoni, sausage, black olives, and mushrooms (2 toppings on each pizza for the children, 1 topping each on the shared pizza)

    # Cost of pizzas before toppings and tip
    total_cost = pizza_ordered * 10  # $10.00 per pizza

    # Cost of toppings
    toppings_cost = toppings_ordered * 1  # $1.00 per topping

    # Cost of tip
    tip_cost = 5  # Ruby gave a $5.00 tip

    # Total cost of pizza order including toppings and tip
    total_cost += toppings_cost + tip_cost
    result = total_cost
    return result

print(solution())