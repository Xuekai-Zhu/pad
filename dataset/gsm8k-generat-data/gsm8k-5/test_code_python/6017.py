def solution():
    mountain_height = 40000  # The mountain is 40,000 feet tall
    fraction_climbed = 3/4  # Stephen climbed 3/4 of the mountain's height on each trip

    # Calculate the total distance Stephen covered on each round trip
    distance_round_trip = mountain_height * fraction_climbed * 2

    # Calculate the total distance Stephen covered on all 10 round trips
    total_distance = distance_round_trip * 10
    result = total_distance
    return result

print(solution())