def solution():
    cheese_price = 5  # Standard price for a cheese pizza
    meat_price = 5  # Standard price for a meat pizza
    cheese_special = 2  # Buy-1-get-1-free special for cheese pizzas
    meat_special = 3  # Buy-2-get-1-free special for meat pizzas
    cheese_pizzas = 10  # Number of cheese pizzas to purchase
    meat_pizzas = 9  # Number of meat pizzas to purchase

    # Calculate the cost of the cheese pizzas after the special
    cheese_discounted = (cheese_pizzas // cheese_special + cheese_pizzas % cheese_special) * cheese_price

    # Calculate the cost of the meat pizzas after the special
    meat_discounted = (meat_pizzas // meat_special + meat_pizzas % meat_special) * meat_price

    # Calculate the total cost of all pizzas
    total_cost = cheese_discounted + meat_discounted
    result = total_cost
    return result

print(solution())