def solution():
    """While preparing balloons for Eva's birthday party, her mom bought 50 balloons and 1800cm³ of helium. One balloon needs 50cm³ to float high enough to touch the ceiling, and she can fill any remaining balloon with ordinary air. If she used up all of the helium and inflated every balloon, how many more balloons are touching the ceiling than not?"""
    # Define the amount of helium needed for one balloon to float
    helium_per_balloon = 50

    # Calculate the maximum number of balloons that can be filled with the given amount of helium
    max_helium_balloons = 1800 // helium_per_balloon

    # Calculate the number of balloons that can be filled with ordinary air
    air_balloons = 50 - max_helium_balloons

    # Calculate the number of balloons that are touching the ceiling
    ceiling_balloons = max_helium_balloons

    # Calculate the number of balloons that are not touching the ceiling
    floor_balloons = 50 - ceiling_balloons

    # Calculate the difference between the number of ceiling balloons and floor balloons
    difference = ceiling_balloons - floor_balloons

    # Return the result
    result = difference
    return result

print(solution())