def solution():
    """A giant spider is discovered.  It weighs 2.5 times the previous largest spider, which weighed 6.4 ounces.  Each of its legs has a cross-sectional area of .5 square inches.  How much pressure in ounces per square inch does each leg undergo?"""
    # Define the weight of the previous largest spider
    PREVIOUS_WEIGHT = 6.4

    # Define the weight of the giant spider
    GIANT_WEIGHT = PREVIOUS_WEIGHT * 2.5

    # Define the cross-sectional area of each leg
    LEG_AREA = 0.5

    # Calculate the total force on all of the spider's legs
    total_force = GIANT_WEIGHT * 16 # convert weight from ounces to pounds

    # Calculate the pressure on each leg
    leg_pressure = total_force / (6 * LEG_AREA) # 6 legs per spider

    # Convert pressure from pounds per square inch to ounces per square inch
    leg_pressure = leg_pressure * 16

    # Display the pressure on each leg
    result = leg_pressure
    return result

print(solution())