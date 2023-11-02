def solution():
    canvas_co2 = 600  # Carbon dioxide released in making the canvas bag, in pounds
    plastic_co2 = 0.25 / 16  # Carbon dioxide released in making one plastic bag, in pounds
    bags_per_trip = 8  # Marla uses 8 plastic bags per shopping trip

    # Calculate the number of shopping trips needed for the canvas bag to be lower-carbon
    trips_needed = canvas_co2 / (plastic_co2 * bags_per_trip)
    result = trips_needed
    return result

print(solution())