def solution():
    """Elizabeth has 20 dollars and wants to buy pens and pencils.
    Each pencil costs $1.60 and each pen cost 2 dollars. How many pencils can she buy with her 20 dollars if she wants 6 pens?"""
    # Define the cost of each item
    PEN_COST = 2
    PENCIL_COST = 1.6

    # Define the number of pens Elizabeth wants to buy
    num_pens = 6

    # Calculate the total cost of the pens
    pen_cost = num_pens * PEN_COST

    # Calculate the maximum number of pencils Elizabeth can buy with the remaining money
    pencils = (20 - pen_cost) // PENCIL_COST

    # Display the number of pencils Elizabeth can buy
    result = pencils
    return result

print(solution())