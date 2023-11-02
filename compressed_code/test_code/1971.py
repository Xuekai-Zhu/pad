def solution():
    
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