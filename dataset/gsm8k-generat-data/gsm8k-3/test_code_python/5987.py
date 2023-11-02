def solution():
    """Marla is thinking about getting a canvas tote bag to avoid using plastic bags at the grocery store. If making the canvas bag released 600 pounds of carbon dioxide, each plastic bag released 4 ounces of carbon dioxide, and Marla uses eight bags per shopping trips, how many shopping trips will she have to make before the canvas bag is the lower-carbon solution? (There are 16 ounces in a pound.)"""
    # Calculate the amount of carbon dioxide released by using eight plastic bags per shopping trip
    plastic_bags_co2 = 8 * 4/16 # convert ounces to pounds

    # Calculate the number of shopping trips needed for using the canvas bag to release less carbon dioxide than using plastic bags
    shopping_trips = 600 / plastic_bags_co2

    # Round up to the nearest whole number of shopping trips
    shopping_trips = math.ceil(shopping_trips)

    # Display the number of shopping trips
    result = shopping_trips
    return result

print(solution())