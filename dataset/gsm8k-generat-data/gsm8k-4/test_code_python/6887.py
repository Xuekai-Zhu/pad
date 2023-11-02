def solution():
    """Amber buys 7 guppies for her pond. Several days later, she sees 3 dozen baby guppies swimming around. Two days after that, she sees 9 more baby guppies. How many guppies does she have now?"""
    # Define the initial number of guppies
    initial_guppies = 7

    # Define the number of baby guppies born after a few days
    baby_guppies_1 = 3 * 12

    # Define the number of baby guppies born two days later
    baby_guppies_2 = 9

    # Calculate the total number of guppies
    total_guppies = initial_guppies + baby_guppies_1 + baby_guppies_2

    # Return the result
    result = total_guppies
    return result

print(solution())