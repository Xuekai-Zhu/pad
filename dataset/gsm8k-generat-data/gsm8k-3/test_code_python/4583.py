def solution():
    """Ruby was going to order pizza for dinner.  Her son would only eat pepperoni pizza.  Her daughter would only eat sausage.  Ruby and her husband wanted black olive and mushroom pizza.  To make life easy, Ruby decided to order an entire pizza for each of her children and she would split one with her husband.  The pizza restaurant charged $10.00 per pizza and $1.00 per topping.  She also needed to add a $5.00 tip.  Including tip, how much would the pizza order cost?"""
    # Define the cost per pizza and per topping
    PIZZA_PRICE = 10
    TOPPING_PRICE = 1

    # Define the number of pizzas and toppings for each type
    son_pizzas = 1
    son_toppings = 1
    daughter_pizzas = 1
    daughter_toppings = 1
    family_pizzas = 0.5
    family_toppings = 2

    # Calculate the total cost of the pizzas and toppings
    son_cost = (son_pizzas * PIZZA_PRICE) + (son_toppings * TOPPING_PRICE)
    daughter_cost = (daughter_pizzas * PIZZA_PRICE) + (daughter_toppings * TOPPING_PRICE)
    family_cost = (family_pizzas * PIZZA_PRICE) + (family_toppings * TOPPING_PRICE)
    total_cost = son_cost + daughter_cost + family_cost + 5

    # Display the total cost
    result = total_cost
    return result

print(solution())