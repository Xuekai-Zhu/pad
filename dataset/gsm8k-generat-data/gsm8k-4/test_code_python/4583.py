def solution():
    """Ruby was going to order pizza for dinner. Her son would only eat pepperoni pizza. Her daughter would only eat sausage. Ruby and her husband wanted black olive and mushroom pizza. To make life easy, Ruby decided to order an entire pizza for each of her children and she would split one with her husband. The pizza restaurant charged $10.00 per pizza and $1.00 per topping. She also needed to add a $5.00 tip. Including tip, how much would the pizza order cost?"""
    # Define the cost of a single pizza and the cost of a topping
    pizza_cost = 10.0
    topping_cost = 1.0

    # Define the number of pizzas ordered for each type
    son_pizzas = 1
    daughter_pizzas = 1
    husband_pizzas = 0.5

    # Define the number of toppings for each pizza
    son_toppings = 1
    daughter_toppings = 1
    husband_toppings = 2

    # Calculate the total cost of the pizzas
    total_pizza_cost = (son_pizzas + daughter_pizzas + husband_pizzas) * pizza_cost

    # Calculate the total cost of the toppings
    total_topping_cost = (son_toppings + daughter_toppings + husband_toppings) * topping_cost

    # Calculate the total cost of the order, including tip
    total_cost = total_pizza_cost + total_topping_cost + 5.0

    # return the result
    result = total_cost
    return result

print(solution())