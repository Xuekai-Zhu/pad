def solution():
    """Caleb has 3 dozen jellybeans. Sophie has half as many jellybeans as Caleb. How many jellybeans do they have in total?"""
    # Define the number of jellybeans in one dozen
    JELLYBEANS_PER_DOZEN = 12

    # Calculate the number of jellybeans Caleb has
    caleb_jellybeans = 3 * JELLYBEANS_PER_DOZEN

    # Calculate the number of jellybeans Sophie has
    sophie_jellybeans = caleb_jellybeans / 2

    # Calculate the total number of jellybeans
    total_jellybeans = caleb_jellybeans + sophie_jellybeans

    # return the result
    result = total_jellybeans
    return result

print(solution())