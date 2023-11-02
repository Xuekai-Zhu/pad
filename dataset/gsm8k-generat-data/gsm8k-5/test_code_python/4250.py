def solution():
    num_friends = 4  # Kingsley is supposed to find 4 friends to help her carry chairs
    chairs_per_trip = 5  # Each student can carry 5 chairs per trip
    num_trips = 10  # Kingsley and her friends will make 10 trips in total

    # Calculate the total number of chairs carried to the school hall
    total_chairs = (num_friends + 1) * chairs_per_trip * num_trips
    result = total_chairs
    return result

print(solution())