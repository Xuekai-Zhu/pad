def solution():
    # Calculate the distance Andy walked to school and back home
    distance_to_school = 50
    distance_from_school_to_home = 50
    total_distance_walked = 140

    # Calculate the distance from home to the market
    distance_to_market = total_distance_walked - distance_to_school - distance_from_school_to_home
    result = distance_to_market
    return result

print(solution())