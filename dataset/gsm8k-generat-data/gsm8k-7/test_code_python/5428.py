def solution():
    distance_to_school = 50
    total_distance = 140
    
    # Calculate the distance from school to market (roundtrip distance)
    distance_school_to_market = (total_distance - distance_to_school) * 2
    
    # Calculate the distance between the house and the market
    distance_between_house_and_market = distance_school_to_market - distance_to_school
    
    result = distance_between_house_and_market
    return result

print(solution())