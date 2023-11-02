def solution():
    """Stanley was standing on the side of the mountain, at an elevation of 10,000 feet, when a gust air blew the comb out of his pocket, causing the comb to fall 4,000 feet to a ledge below. Stanley's brother, Oliver, was also on the mountain, but he was at an elevation of 3,000 feet. Stanley called Oliver on his cellphone and asked Oliver to find Stanley's comb. How many feet must Oliver climb to reach the elevation of Stanley's comb?"""
    stanley_elevation = 10000
    comb_elevation = 4000
    oliver_elevation = 3000
    distance_to_climb = stanley_elevation - comb_elevation - oliver_elevation
    result = distance_to_climb
    return result

print(solution())