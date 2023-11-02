def solution():
    """Kingsley's teacher instructed her to find four friends to help her carry some chairs to the school hall to be used for an upcoming event. If each student carried 5 chairs per trip and made 10 trips in total, what's the total number of chairs taken to the hall?"""
    # Define the number of friends helping Kingsley
    num_friends = 4

    # Define the number of chairs each student can carry per trip
    chairs_per_trip = 5

    # Define the number of trips made by each student
    trips_per_student = 10

    # Calculate the total number of chairs taken to the hall
    total_chairs = num_friends * chairs_per_trip * trips_per_student

    # Return the result
    result = total_chairs
    return result

print(solution())