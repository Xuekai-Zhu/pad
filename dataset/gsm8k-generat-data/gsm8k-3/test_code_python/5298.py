def solution():
    """Carla works at a food bank and she currently has stocked up 2000 cans of food. One day, 500 people showed up and took 1 can of food each. Carla had to then restock 1500 more cans to keep up with demand. The next day, 1000 people showed up and took 2 cans of food each. Carla restocked again with 3000 cans of food this time. How many cans of food did Carla give away?"""
    # Define the initial stock and the number of people who showed up each day
    INITIAL_STOCK = 2000
    DAY_ONE_PEOPLE = 500
    DAY_TWO_PEOPLE = 1000

    # Calculate the cans given away on day one
    day_one_giveaway = DAY_ONE_PEOPLE * 1

    # Calculate the final stock after day one
    day_one_stock = INITIAL_STOCK - day_one_giveaway + 1500

    # Calculate the cans given away on day two
    day_two_giveaway = DAY_TWO_PEOPLE * 2

    # Calculate the final stock after day two
    final_stock = day_one_stock - day_two_giveaway + 3000

    # Calculate the total number of cans Carla gave away
    cans_given_away = INITIAL_STOCK - final_stock

    # Display the total number of cans given away
    result = cans_given_away
    return result

print(solution())