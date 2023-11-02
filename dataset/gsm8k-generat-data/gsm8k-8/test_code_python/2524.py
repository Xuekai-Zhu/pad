def solution():
    # Calculate the total number of balloons that can be inflated with the given amount of helium
    helium_volume_per_balloon = 50
    total_helium_balloons = 1800 // helium_volume_per_balloon

    # Calculate the total number of balloons that can be inflated with ordinary air
    total_balloons = 50
    total_air_balloons = total_balloons - total_helium_balloons

    # Calculate the number of balloons that are touching the ceiling
    ceiling_balloons = total_helium_balloons

    # Calculate the number of balloons that are not touching the ceiling
    floor_balloons = total_air_balloons

    # Calculate the difference between the number of balloons touching the ceiling and not touching the ceiling
    difference = ceiling_balloons - floor_balloons
    result = difference
    return result

print(solution())