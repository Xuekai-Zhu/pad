def solution():
    """A giant spider is discovered. It weighs 2.5 times the previous largest spider, which weighed 6.4 ounces. Each of its legs has a cross-sectional area of .5 square inches. How much pressure in ounces per square inch does each leg undergo?"""
    # Define the weight of the previous largest spider and the weight of the giant spider
    prev_spider_weight = 6.4
    giant_spider_weight = 2.5 * prev_spider_weight

    # Define the cross-sectional area of each leg
    leg_area = 0.5

    # Calculate the total force on each leg
    leg_force = giant_spider_weight / 8

    # Calculate the pressure on each leg
    leg_pressure = leg_force / leg_area

    # Convert the pressure to ounces per square inch
    pressure_ounces = leg_pressure * 16

    # Return the result
    result = pressure_ounces
    return result

print(solution())