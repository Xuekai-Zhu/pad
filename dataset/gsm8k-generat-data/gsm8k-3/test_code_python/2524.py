def solution():
    """While preparing balloons for Eva's birthday party, her mom bought 50 balloons and 1800cm³ of helium. One balloon needs 50cm³ to float high enough to touch the ceiling, and she can fill any remaining balloon with ordinary air. If she used up all of the helium and inflated every balloon, how many more balloons are touching the ceiling than not?"""
    # Define the volume of helium needed for each balloon to touch the ceiling
    HELIUM_VOLUME = 50

    # Calculate the maximum number of balloons that can be filled with the given amount of helium
    max_balloons = 1800 // HELIUM_VOLUME

    # Calculate the number of balloons that can be filled with helium
    helium_balloons = min(max_balloons, 50)

    # Calculate the number of balloons that can be filled with ordinary air
    air_balloons = 50 - helium_balloons

    # Calculate the number of balloons that are touching the ceiling
    ceiling_balloons = helium_balloons

    # Calculate the number of balloons that are not touching the ceiling
    non_ceiling_balloons = air_balloons

    # Calculate the difference between the number of balloons touching the ceiling and not touching the ceiling
    difference = ceiling_balloons - non_ceiling_balloons

    # Display the difference
    result = difference
    return result

print(solution())