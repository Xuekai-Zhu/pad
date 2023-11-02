def solution():
    """Mary Anne drinks 1/5 of a bottle of sparkling water every night at dinner.  If each bottle costs her $2.00, how much does she spend on sparkling water every year?"""
    # Define the fraction of a bottle Mary Anne drinks each night
    fraction_per_night = 1/5

    # Define the cost of each bottle
    cost_per_bottle = 2.00

    # Calculate the total number of bottles Mary Anne drinks in a year
    bottles_per_year = 365 * fraction_per_night

    # Calculate the total cost of the sparkling water Mary Anne drinks in a year
    total_cost = bottles_per_year * cost_per_bottle

    # Display the total cost
    result = total_cost
    return result

print(solution())