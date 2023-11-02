def solution():
    """Jimmy wants to order a pizza at a new place. The large pizza costs $10.00 and is cut into 8 slices. The first topping costs $2.00, the next 2 toppings cost $1.00 each and the rest of the toppings cost $0.50. If he orders a large pizza with pepperoni, sausage, ham, olives, mushrooms, bell peppers and pineapple. How much will his pizza cost per slice?"""
    # Define the cost of the pizza and toppings
    pizza_cost = 10.00
    first_topping_cost = 2.00
    second_topping_cost = 1.00
    rest_topping_cost = 0.50
    
    # Define the number of toppings
    num_toppings = 7
    
    # Calculate the total cost of the toppings
    total_toppings_cost = (first_topping_cost) + (2 * second_topping_cost) + ((num_toppings - 3) * rest_topping_cost)
    
    # Calculate the total cost of the pizza with toppings
    total_cost = pizza_cost + total_toppings_cost
    
    # Calculate the cost per slice
    cost_per_slice = total_cost / 8
    
    # Return the result rounded to 2 decimal places
    result = round(cost_per_slice, 2)
    return result

print(solution())