def solution():
    """Kylie has 5 daisies. Her sister gave her another 9 daisies. Kylie then gave half her daisies to her mother. How many daisies does Kylie have left?"""
    # Define the initial number of daisies Kylie has
    kylie_daisies = 5

    # Define the number of daisies Kylie's sister gave her
    sister_daisies = 9

    # Add the number of daisies Kylie received from her sister
    kylie_daisies += sister_daisies

    # Calculate the number of daisies Kylie gave her mother
    mother_daisies = kylie_daisies // 2

    # Subtract the number of daisies Kylie gave her mother from her total number of daisies
    kylie_daisies -= mother_daisies

    result = kylie_daisies
    return result

print(solution())