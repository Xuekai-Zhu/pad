def solution():
    """Marcus can fit 5 pies in his oven at once. He bakes 7 batches of pies, then slips and drops 8 of them. How many pies are left?"""
    # Define the number of pies Marcus can fit in his oven at once
    MAX_PIES = 5

    # Define the number of batches of pies Marcus bakes
    num_batches = 7

    # Calculate the total number of pies Marcus bakes
    total_pies = num_batches * MAX_PIES

    # Subtract the number of pies Marcus dropped
    pies_left = total_pies - 8

    # Display the number of pies left
    result = pies_left
    return result

print(solution())