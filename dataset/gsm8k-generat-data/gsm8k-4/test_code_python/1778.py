def solution():
    """Dorothy spent $53 to buy doughnut ingredients. If she made 25 doughnuts and sells each for $3, how much was her profit?"""
    # Define the cost of ingredients
    ingredients_cost = 53

    # Define the number of doughnuts made
    doughnuts_made = 25

    # Define the price per doughnut
    doughnut_price = 3

    # Calculate the revenue from selling the doughnuts
    revenue = doughnuts_made * doughnut_price

    # Calculate the profit from selling the doughnuts
    profit = revenue - ingredients_cost

    result = profit
    return result

print(solution())