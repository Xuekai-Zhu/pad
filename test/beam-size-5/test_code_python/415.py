def solution():
    
    stanley_elevation = 10000
    gust_air_blew = 4000
    oliver_elevation = 3000
    total_elevation = stanley_elevation + oliver_elevation
    climb_elevation = total_elevation - stanley_elevation
    result = climb_elevation
    return result

print(solution())