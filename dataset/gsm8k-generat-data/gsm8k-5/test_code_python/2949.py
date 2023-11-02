def solution():
    # Calculate the total time used by all family members in the bathroom
    total_time_used = 45 + 30 + 20  # Oldest daughter used for 45 mins, youngest daughter for 30 mins and husband for 20 mins

    # Calculate the time remaining until 5 pm
    time_remaining = (5 - 2.5) * 60  # 5 pm - 2:30 pm = 2.5 hours, converted to minutes

    # Calculate the time Mrs. Parker has left to use the bathroom
    time_left = time_remaining - total_time_used
    result = time_left
    return result

print(solution())