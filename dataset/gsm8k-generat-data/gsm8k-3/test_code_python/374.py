def solution():
    """TJ ran a 10K race last Saturday. He ran the first half in 20 minutes. He completed the second half in 30 minutes. What was his average time per kilometer?"""
    # Convert the times to seconds
    time1 = 20 * 60
    time2 = 30 * 60

    # Calculate the total time in seconds
    total_time = time1 + time2

    # Calculate the total distance in kilometers
    distance = 10

    # Calculate the average time per kilometer
    average_time = total_time / (distance * 2)

    # Convert the average time back to minutes and seconds
    minutes = int(average_time / 60)
    seconds = int(average_time % 60)

    # Display the result
    result = f"{minutes}:{seconds:02d}"
    return result

print(solution())