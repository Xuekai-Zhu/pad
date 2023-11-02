def solution():
    """Each year a store decreased the price of a certain model of TV by $35. If the price in 2001 was $1950, what was the price in 2009?"""
    # Define the initial price and the number of years
    initial_price = 1950
    years = 8

    # Calculate the final price after 8 years of decreasing the price by $35 each year
    final_price = initial_price - (35 * years)

    # Return the final price
    result = final_price
    return result

print(solution())