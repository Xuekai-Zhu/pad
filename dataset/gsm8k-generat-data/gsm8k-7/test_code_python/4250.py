def solution():
    num_students = 5  # Kingsley plus four friends
    chairs_per_trip = 5
    num_trips = 10

    # Calculate the total number of chairs taken to the hall
    total_chairs = num_students * chairs_per_trip * num_trips
    result = total_chairs
    return result

print(solution())