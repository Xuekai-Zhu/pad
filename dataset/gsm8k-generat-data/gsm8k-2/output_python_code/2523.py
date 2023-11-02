def solution():
    """While preparing balloons for Eva's birthday party, her mom bought 50 balloons and 1800cm³ of helium.
    One balloon needs 50cm³ to float high enough to touch the ceiling, and she can fill any remaining balloon with ordinary air.
    If she used up all of the helium and inflated every balloon, how many more balloons are touching the ceiling than not?"""
    total_helium = 1800
    helium_per_balloon = 50
    balloons = 50
    helium_balloons = total_helium // helium_per_balloon
    ordinary_balloons = balloons - helium_balloons
    balloons_touching_ceiling = helium_balloons
    balloons_not_touching_ceiling = ordinary_balloons
    difference = balloons_touching_ceiling - balloons_not_touching_ceiling
    result = difference
    return result

print(solution())