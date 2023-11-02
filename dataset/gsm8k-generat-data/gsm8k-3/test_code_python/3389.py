def solution():
    """A certain store sells computer accessories and equipment. Due to a fire outbreak in one of the factories, the price of RAM increased by 30%. After two years, the price stabilized and finally fell by 20% from what it has risen. What is the current price of RAM if it was $50 before the fire?"""
    # Define the initial price of the RAM
    initial_price = 50

    # Calculate the increased price after the fire outbreak
    increased_price = initial_price * 1.3

    # Calculate the stabilized price after two years
    stabilized_price = increased_price

    # Calculate the final price after the 20% decrease
    final_price = stabilized_price * 0.8

    # Display the current price of RAM
    result = final_price
    return result

print(solution())