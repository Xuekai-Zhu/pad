def solution():
    """A certain store sells computer accessories and equipment. Due to a fire outbreak in one of the factories, the price of RAM increased by 30%. After two years, the price stabilized and finally fell by 20% from what it has risen. What is the current price of RAM if it was $50 before the fire?"""
    # Define the initial price of RAM
    initial_price = 50

    # Calculate the price increase due to the fire
    price_increase = initial_price * 0.3

    # Calculate the price of RAM after the fire
    price_after_fire = initial_price + price_increase

    # Calculate the price reduction after two years
    price_reduction = price_increase * 0.2

    # Calculate the current price of RAM
    current_price = price_after_fire - price_reduction

    # Return the result
    result = current_price
    return result

print(solution())