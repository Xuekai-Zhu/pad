def solution():
    """Emery's family decides to travel for a weekend trip. They drive the first 100 miles in 1 hour. They stop at a McDonald's and then continue the rest of the journey for 300 miles. What's the total number of hours they traveled?"""
    # Define the total distance traveled
    total_distance = 400

    # Define the time taken to travel the first 100 miles
    time1 = 1

    # Define the time taken to travel the remaining 300 miles
    time2 = 300 / 60

    # Calculate the total time taken
    total_time = time1 + time2

    # Display the total time taken
    result = total_time
    return result

print(solution())