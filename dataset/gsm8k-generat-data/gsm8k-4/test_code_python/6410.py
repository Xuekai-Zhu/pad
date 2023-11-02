def solution():
    """Moore's family compared mobile phone plans to get the best deal. At T-Mobile, the family plan costs $50 per month for the first two lines and $16 for each additional line. 
    At M-Mobile, the family plan costs $45 for the first two lines and $14 for each additional line. Moore's family needs to purchase 5 cell phone lines. 
    How much cheaper is the M-Mobile than T-Mobile?"""
    # Define the prices for T-Mobile and M-Mobile plans
    tmobile_first_two = 50
    tmobile_additional = 16
    mmobile_first_two = 45
    mmobile_additional = 14

    # Calculate the total cost of a 5-line family plan for T-Mobile
    tmobile_cost = tmobile_first_two + tmobile_additional * 3

    # Calculate the total cost of a 5-line family plan for M-Mobile
    mmobile_cost = mmobile_first_two + mmobile_additional * 3

    # Calculate the difference in cost between the two plans
    cost_difference = tmobile_cost - mmobile_cost

    # Return the result
    result = cost_difference
    return result

print(solution())