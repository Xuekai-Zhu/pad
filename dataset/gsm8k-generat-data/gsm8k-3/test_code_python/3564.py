def solution():
    """Tina buys a loaf of bread for $50, 2oz of ham for $150, and a cake for $200. What percent of the cost is the ham and bread?"""
    # Define the cost of each item
    BREAD_COST = 50
    HAM_COST = 150
    CAKE_COST = 200

    # Calculate the total cost of the bread and ham
    total_cost = BREAD_COST + HAM_COST

    # Calculate the percentage of the total cost that is the bread and ham
    percent_cost = (total_cost / (BREAD_COST + HAM_COST + CAKE_COST)) * 100

    # Display the percentage of cost that is the bread and ham
    result = percent_cost
    return result

print(solution())