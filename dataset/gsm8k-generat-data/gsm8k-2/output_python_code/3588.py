def solution():
    """Danny is bringing his sailboat out to the ocean. When he uses his 24 square foot sail he goes 50 MPH. When he uses his 12 square foot sail he goes 20 MPH. 
    He plans to travel 200 miles. How many hours faster is the bigger sail than the smaller one?"""
    distance_to_travel = 200
    speed_big_sail = 50
    speed_small_sail = 20
    time_big_sail = distance_to_travel / speed_big_sail
    time_small_sail = distance_to_travel / speed_small_sail
    time_difference = time_small_sail - time_big_sail
    result = time_difference
    return result

print(solution())