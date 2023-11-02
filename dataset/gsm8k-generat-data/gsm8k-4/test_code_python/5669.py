def solution():
    """Jett bought a cow from the market at $600 and took it to his farm. He spent $20 every day to buy food. He also used $500 to vaccinate and deworm the cow. If he sold the cow for $2500 after 40 days, calculate the profit he made from selling back the cow to the market."""
    # Define the initial cost of purchasing the cow and the cost of vaccination
    INITIAL_COST = 600
    VACCINATION_COST = 500

    # Define the daily cost of feeding the cow
    DAILY_FEED_COST = 20

    # Define the selling price of the cow
    SELLING_PRICE = 2500

    # Calculate the total cost of owning the cow for 40 days
    total_cost = INITIAL_COST + VACCINATION_COST + (DAILY_FEED_COST * 40)

    # Calculate the profit Jett made from selling the cow
    profit = SELLING_PRICE - total_cost

    # Return the result
    result = profit
    return result

print(solution())