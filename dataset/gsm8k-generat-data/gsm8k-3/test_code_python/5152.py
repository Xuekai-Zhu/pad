def solution():
    """Jimmy wants to order a pizza at a new place. The large pizza costs $10.00 and is cut into 8 slices. The first topping costs $2.00, the next 2 toppings cost $1.00 each and the rest of the toppings cost $0.50. If he orders a large pizza with pepperoni, sausage, ham, olives, mushrooms, bell peppers and pineapple. How much will his pizza cost per slice?"""
    
    # Define the cost of the pizza and the number of slices
    pizza_cost = 10.00
    num_slices = 8

    # Define the cost of the toppings
    first_topping_cost = 2.00
    second_topping_cost = 1.00
    other_topping_cost = 0.50

    # Define the number of each type of topping that Jimmy wants
    num_pepperoni = 1
    num_sausage = 1
    num_ham = 1
    num_olives = 1
    num_mushrooms = 1
    num_bell_peppers = 1
    num_pineapple = 1

    # Calculate the total cost of the pizza with toppings
    total_cost = pizza_cost + (first_topping_cost + (num_slices-1)*other_topping_cost) + (num_pepperoni + num_sausage + num_ham + num_olives + num_mushrooms + num_bell_peppers + num_pineapple - 1)*second_topping_cost

    # Calculate the cost per slice
    cost_per_slice = total_cost / num_slices

    # Display the cost per slice
    result = round(cost_per_slice, 2)
    return result

print(solution())