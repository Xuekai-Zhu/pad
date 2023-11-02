def solution():
    """A factory produced televisions at a constant rate of 10 per day in a certain year. If they reduced the total production by 10 percent in the second year, calculate the total production of television by the factory in the second year."""
    # Define the constant rate of production and the reduction percentage
    production_rate = 10
    reduction_percent = 0.1

    # Calculate the total production in the first year (365 days)
    total_production_year_1 = production_rate * 365

    # Calculate the reduced total production in the second year (365 days)
    reduced_production_rate = production_rate * (1 - reduction_percent)
    total_production_year_2 = reduced_production_rate * 365

    # Return the result
    result = total_production_year_2
    return result

print(solution())