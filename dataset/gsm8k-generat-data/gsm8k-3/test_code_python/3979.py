def solution():
    """Mr. Alvarez spends $36 on diesel fuel each week. If the cost of diesel fuel is $3 per gallon, how many gallons of diesel fuel does Mr. Alvarez use in two weeks?"""
    # Define the cost of diesel fuel per gallon
    COST_PER_GALLON = 3

    # Define the amount Mr. Alvarez spends on diesel fuel in two weeks
    total_cost = 36 * 2

    # Calculate the number of gallons of diesel fuel used in two weeks
    gallons_used = total_cost / COST_PER_GALLON

    # Display the number of gallons used
    result = gallons_used
    return result

print(solution())