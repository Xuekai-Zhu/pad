def solution():
    """In Zeoland the fine for speeding is $16 for each mile per hour the driver is traveling over the posted speed limit. In Zeoland, Jed was fined $256 for speeding on a road with a posted speed limit of 50 mph. Jed was fined for traveling at what speed in miles per hour?"""
    # Define the posted speed limit and the fine per mph over the limit
    speed_limit = 50
    fine_per_mph = 16

    # Calculate the amount Jed was fined over the posted speed limit
    fine_over_limit = 256 - (speed_limit * fine_per_mph)

    # Calculate the speed at which Jed was fined
    jed_speed = speed_limit + (fine_over_limit / fine_per_mph)

    # Round the speed to the nearest whole number
    rounded_speed = round(jed_speed)

    # return the result
    result = rounded_speed
    return result

print(solution())