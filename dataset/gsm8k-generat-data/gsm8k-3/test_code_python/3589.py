def solution():
    """Danny is bringing his sailboat out to the ocean. When he uses his 24 square foot sail he goes 50 MPH. When he uses his 12 square foot sail he goes 20 MPH. He plans to travel 200 miles. How many hours faster is the bigger sail than the smaller one?"""
    # Define the sail areas and speeds
    BIG_SAIL_AREA = 24
    SMALL_SAIL_AREA = 12
    BIG_SAIL_SPEED = 50
    SMALL_SAIL_SPEED = 20

    # Define the distance to travel
    distance = 200

    # Calculate the time to travel with the big sail
    big_sail_time = distance / BIG_SAIL_SPEED

    # Calculate the time to travel with the small sail
    small_sail_time = distance / SMALL_SAIL_SPEED

    # Calculate the time difference
    time_difference = small_sail_time - big_sail_time

    # Display the time difference
    result = time_difference
    return result

print(solution())