def solution():
    # Calculate the total driving time for Jenna and her friend
    jenna_driving_time = 200 / 50  # Jenna drives the first 200 miles at 50 miles per hour
    friend_driving_time = 100 / 20  # Jenna's friend drives the last 100 miles at 20 miles per hour
    total_driving_time = jenna_driving_time + friend_driving_time  # Total time spent driving

    # Add in time for the two 30-minute breaks
    total_driving_time += 1/2 + 1/2

    result = total_driving_time
    return result

print(solution())