def solution():
    """Carla works at a food bank and she currently has stocked up 2000 cans of food. One day, 500 people showed up and took 1 can of food each.
    Carla had to then restock 1500 more cans to keep up with demand. The next day, 1000 people showed up and took 2 cans of food each. Carla restocked
    again with 3000 cans of food this time. How many cans of food did Carla give away?"""
    # Define the initial number of cans of food
    initial_cans = 2000

    # Calculate the number of cans given away on the first day
    day1_cans_given = 500

    # Calculate the number of cans restocked after the first day
    day1_cans_restocked = 1500

    # Calculate the number of cans given away on the second day
    day2_cans_given = 1000 * 2

    # Calculate the number of cans restocked after the second day
    day2_cans_restocked = 3000

    # Calculate the total number of cans given away
    total_cans_given = day1_cans_given + day2_cans_given

    # Return the result
    result = total_cans_given
    return result

print(solution())