def solution():
    """Each year a store decreased the price of a certain model of TV by $35. If the price in 2001 was $1950, what was the price in 2009?"""
    # Define the initial price and the number of years
    initial_price = 1950
    num_years = 8   # From 2001 to 2009 (inclusive)

    # Calculate the final price after the price decrease each year
    final_price = initial_price - (35 * num_years)

    # Display the final price
    result = final_price
    return result

print(solution())