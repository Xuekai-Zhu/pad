def solution():
    """Jimmy wants to order a pizza at a new place. The large pizza costs $10.00 and is cut into 8 slices. The first topping costs $2.00, the next 2 toppings cost $1.00 each and the rest of the toppings cost $0.50. If he orders a large pizza with pepperoni, sausage, ham, olives, mushrooms, bell peppers and pineapple. How much will his pizza cost per slice?"""
    pizza_cost = 10
    num_slices = 8
    num_toppings = 7
    topping_cost = 2 + 1 + 1 + (num_toppings - 3) * 0.5
    total_cost = pizza_cost + topping_cost
    cost_per_slice = total_cost / num_slices
    result = cost_per_slice
    return result

print(solution())