def solution():
    """Ruby was going to order pizza for dinner. Her son would only eat pepperoni pizza. Her daughter would only eat sausage. Ruby and her husband wanted black olive and mushroom pizza. To make life easy, Ruby decided to order an entire pizza for each of her children and she would split one with her husband. The pizza restaurant charged $10.00 per pizza and $1.00 per topping. She also needed to add a $5.00 tip. Including tip, how much would the pizza order cost?"""
    total_pizzas = 3
    toppings_per_pizza = 2
    cost_per_pizza = 10
    cost_per_topping = 1
    tip = 5
    total_cost = (total_pizzas * cost_per_pizza) + (toppings_per_pizza * total_pizzas * cost_per_topping) + tip
    result = total_cost
    return result

print(solution())