def solution():
    """Samuel is driving to San Francisco’s Comic-Con in his car and he needs to travel 600 miles to the hotel where he made a reservation. At first, he drives at 50 miles/hour for 3 hours straight, then he speeds up to 80 miles/hour for 4 hours. How far is he from the hotel?"""
    # Calculate the distance covered in the first leg of the trip
    distance_leg1 = 50 * 3

    # Calculate the distance covered in the second leg of the trip
    distance_leg2 = 80 * 4

    # Calculate the total distance covered
    total_distance = distance_leg1 + distance_leg2

    # Calculate the remaining distance to the hotel
    remaining_distance = 600 - total_distance

    # Return the remaining distance
    result = remaining_distance
    return result

print(solution())