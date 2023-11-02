def solution():
     total_balloons = 50
     total_helium = 1800
     helium_per_balloon = 50
     balloons_floating = total_helium / helium_per_balloon
     balloons_not_floating = total_balloons - balloons_floating
     result = balloons_floating - balloons_not_floating
     return result

print(solution())