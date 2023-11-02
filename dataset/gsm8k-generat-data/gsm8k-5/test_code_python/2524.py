def solution():
    total_helium = 1800  # Eva's mom has 1800cm³ of helium
    helium_per_balloon = 50  # One balloon needs 50cm³ of helium to touch the ceiling
    total_balloons = 50  # Eva's mom bought 50 balloons
    balloons_with_helium = total_helium // helium_per_balloon  # Calculate the number of balloons that can be filled with helium
    balloons_with_air = total_balloons - balloons_with_helium  # Calculate the number of balloons that need to be filled with air

    # Calculate the number of balloons that are touching the ceiling
    balloons_touching_ceiling = min(balloons_with_helium, total_balloons)
    balloons_not_touching_ceiling = total_balloons - balloons_touching_ceiling + balloons_with_air

    # Calculate the difference between the balloons touching and not touching the ceiling
    difference = abs(balloons_touching_ceiling - balloons_not_touching_ceiling)
    result = difference
    return result

print(solution())