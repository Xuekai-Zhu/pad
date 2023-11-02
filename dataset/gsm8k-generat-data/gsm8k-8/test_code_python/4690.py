def solution():
    # Define variables
    speed = 40
    distance = 60
    # Calculate the time for one way
    time = distance / speed
    # Calculate the round trip time
    round_trip_time = time * 2
    result = round_trip_time
    return result

print(solution())