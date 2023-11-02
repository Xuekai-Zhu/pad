def solution():
    """There are 120 crayons in a box.  One third of the crayons are new, 20% are broken, and the rest are slightly used.  How many are slightly used?"""
    # Define the total number of crayons
    total_crayons = 120

    # Calculate the number of new crayons
    new_crayons = total_crayons // 3

    # Calculate the number of broken crayons
    broken_crayons = total_crayons * 0.2

    # Calculate the number of slightly used crayons
    slightly_used_crayons = total_crayons - new_crayons - broken_crayons

    result = slightly_used_crayons
    return result

print(solution())