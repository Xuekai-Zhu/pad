def solution():
    # Calculate the weight of the giant spider
    giant_spider_weight = 2.5 * 6.4

    # Calculate the total area of all the spider's legs
    total_leg_area = 8 * 0.5

    # Calculate the pressure per leg
    pressure_per_leg = giant_spider_weight / total_leg_area

    # Convert pressure to ounces per square inch
    pressure_ounces_per_square_inch = pressure_per_leg / 16

    result = pressure_ounces_per_square_inch

    return result

print(solution())