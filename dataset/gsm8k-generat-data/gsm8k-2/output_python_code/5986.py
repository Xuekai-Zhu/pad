def solution():
    """Marla is thinking about getting a canvas tote bag to avoid using plastic bags at the grocery store. If making the canvas bag released 600 pounds of carbon dioxide, each plastic bag released 4 ounces of carbon dioxide, and Marla uses eight bags per shopping trips, how many shopping trips will she have to make before the canvas bag is the lower-carbon solution? (There are 16 ounces in a pound.)"""
    canvas_c02 = 600
    plastic_c02_per_bag = 4 / 16  # in pounds
    bags_per_trip = 8
    trips = canvas_c02 / (bags_per_trip * plastic_c02_per_bag)
    result = trips
    return result

print(solution())