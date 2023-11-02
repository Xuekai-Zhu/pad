def solution():
    """Marla is thinking about getting a canvas tote bag to avoid using plastic bags at the grocery store. If making the canvas bag released 600 pounds of carbon dioxide, each plastic bag released 4 ounces of carbon dioxide, and Marla uses eight bags per shopping trips, how many shopping trips will she have to make before the canvas bag is the lower-carbon solution? (There are 16 ounces in a pound.)"""
    canvas_co2 = 600
    plastic_co2 = 4/16 # converting 4 ounces to pounds
    bags_per_trip = 8
    trips = canvas_co2 / (bags_per_trip * plastic_co2)
    result = trips
    return result

print(solution())