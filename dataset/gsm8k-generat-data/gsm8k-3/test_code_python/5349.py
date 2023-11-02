def solution():
    """Samuel is driving to San Francisco’s Comic-Con in his car and he needs to travel 600 miles to the hotel where he made a reservation. At first, he drives at 50 miles/hour for 3 hours straight, then he speeds up to 80 miles/hour for 4 hours. How far is he from the hotel?"""
    # Calculate the distance traveled in the first 3 hours
    distance1 = 50 * 3

    # Calculate the distance traveled in the next 4 hours
    distance2 = 80 * 4

    # Calculate the total distance traveled
    total_distance = distance1 + distance2

    # Calculate the remaining distance to the hotel
    remaining_distance = 600 - total_distance

    # Display the remaining distance
    result = remaining_distance
    return result

print(solution())