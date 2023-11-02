def solution():
    """Bruno wants to buy two and one-half dozens of pens. How many pens will he have?"""
    # Define the number of pens in one dozen
    PENS_PER_DOZEN = 12

    # Define the number of dozens Bruno wants to buy
    num_dozens = 2.5

    # Calculate the total number of pens
    total_pens = num_dozens * PENS_PER_DOZEN

    # Return the result
    result = total_pens
    return result

print(solution())