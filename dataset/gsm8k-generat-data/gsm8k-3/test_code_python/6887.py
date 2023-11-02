def solution():
    """Amber buys 7 guppies for her pond.  Several days later, she sees 3 dozen baby guppies swimming around.  Two days after that, she sees 9 more baby guppies.  How many guppies does she have now?"""
    # Define the initial number of guppies
    initial_guppies = 7

    # Calculate the number of baby guppies from the first sighting
    baby_guppies1 = 3 * 12

    # Calculate the total number of guppies after the first sighting
    total_guppies1 = initial_guppies + baby_guppies1

    # Calculate the number of baby guppies from the second sighting
    baby_guppies2 = 9

    # Calculate the total number of guppies after the second sighting
    total_guppies2 = total_guppies1 + baby_guppies2

    # Display the total number of guppies
    result = total_guppies2
    return result

print(solution())