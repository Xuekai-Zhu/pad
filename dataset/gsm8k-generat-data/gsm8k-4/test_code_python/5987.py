def solution():
    """Marla is thinking about getting a canvas tote bag to avoid using plastic bags at the grocery store. If making the canvas bag released 600 pounds of carbon dioxide, each plastic bag released 4 ounces of carbon dioxide, and Marla uses eight bags per shopping trips, how many shopping trips will she have to make before the canvas bag is the lower-carbon solution? (There are 16 ounces in a pound.)"""
    # Define the carbon emissions of a canvas bag and a plastic bag
    CANVAS_EMISSIONS = 600
    PLASTIC_EMISSIONS = 4 / 16

    # Define the number of bags used per shopping trip
    BAGS_PER_TRIP = 8

    # Calculate the number of shopping trips needed to make the canvas bag the lower-carbon solution
    trips_needed = CANVAS_EMISSIONS / (PLASTIC_EMISSIONS * BAGS_PER_TRIP)

    # Round up to the nearest whole number of shopping trips
    trips_needed = int(math.ceil(trips_needed))

    result = trips_needed
    return result

print(solution())