def solution():
    """Danny is bringing his sailboat out to the ocean. When he uses his 24 square foot sail he goes 50 MPH. When he uses his 12 square foot sail he goes 20 MPH. He plans to travel 200 miles. How many hours faster is the bigger sail than the smaller one?"""
    # Define the sail areas and velocities
    big_sail_area = 24
    big_sail_speed = 50
    small_sail_area = 12
    small_sail_speed = 20

    # Define the distance to be traveled
    distance = 200

    # Calculate the time it will take with the big sail
    big_sail_time = distance / big_sail_speed

    # Calculate the time it will take with the small sail
    small_sail_time = distance / small_sail_speed

    # Calculate the time difference between the two sails
    time_difference = small_sail_time - big_sail_time

    # Return the hours faster that the big sail is than the small sail
    result = abs(time_difference)
    return result

print(solution())