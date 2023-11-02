def solution():
    # Calculate the maximum number of balloons that can be filled with helium using the given amount of helium
    max_helium_balloons = 1800 // 50

    # Calculate the number of balloons that can be filled with ordinary air
    air_balloons = 50 - max_helium_balloons

    # Calculate the number of balloons that are touching the ceiling
    ceiling_balloons = max_helium_balloons

    # Calculate the number of balloons that are not touching the ceiling
    non_ceiling_balloons = 50 - max_helium_balloons

    # Calculate the difference between the number of balloons touching the ceiling and the number of balloons not touching the ceiling
    difference = ceiling_balloons - non_ceiling_balloons

    result = difference
    return result

print(solution())