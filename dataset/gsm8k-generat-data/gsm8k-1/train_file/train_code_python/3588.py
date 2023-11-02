def solution():
    """Danny is bringing his sailboat out to the ocean. When he uses his 24 square foot sail he goes 50 MPH. When he uses his 12 square foot sail he goes 20 MPH. He plans to travel 200 miles. How many hours faster is the bigger sail than the smaller one?"""
    distance = 200
    speed_24 = 50
    speed_12 = 20
    time_24 = distance / speed_24
    time_12 = distance / speed_12
    time_difference = time_12 - time_24
    result = time_difference
    return result

print(solution())