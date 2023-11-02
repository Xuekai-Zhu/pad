def solution():
    """Caleb has 3 dozen jellybeans.  Sophie has half as many jellybeans as Caleb.  How many jellybeans do they have in total?"""
    # Define the number of jellybeans in a dozen
    JELLYBEANS_PER_DOZEN = 12

    # Define the number of dozens of jellybeans that Caleb has
    caleb_dozens = 3

    # Calculate the total number of jellybeans that Caleb has
    caleb_jellybeans = caleb_dozens * JELLYBEANS_PER_DOZEN

    # Calculate the number of jellybeans that Sophie has (half as many as Caleb)
    sophie_jellybeans = caleb_jellybeans / 2

    # Calculate the total number of jellybeans they have together
    total_jellybeans = caleb_jellybeans + sophie_jellybeans

    # Display the total number of jellybeans
    result = total_jellybeans
    return result

print(solution())