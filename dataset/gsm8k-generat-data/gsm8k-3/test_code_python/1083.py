def solution():
    """A factory produced televisions at a constant rate of 10 per day in a certain year. If they reduced the total production by 10 percent in the second year, calculate the total production of television by the factory in the second year."""
    # Define the production rate per day and the reduction percentage
    PRODUCTION_RATE = 10
    REDUCTION_PERCENTAGE = 0.1

    # Calculate the total production in the first year
    total_production_year1 = PRODUCTION_RATE * 365

    # Calculate the reduction in total production for the second year
    reduction = total_production_year1 * REDUCTION_PERCENTAGE

    # Calculate the total production in the second year
    total_production_year2 = total_production_year1 - reduction

    # Display the total production in the second year
    result = total_production_year2
    return result

print(solution())