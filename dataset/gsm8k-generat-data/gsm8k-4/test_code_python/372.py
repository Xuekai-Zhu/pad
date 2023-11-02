def solution():
    """TJ ran a 10K race last Saturday. He ran the first half in 20 minutes. He completed the second half in 30 minutes. What was his average time per kilometer?"""
    # Define the total distance in kilometers
    total_distance = 10

    # Calculate the total time taken to complete the race
    total_time = 20 + 30

    # Calculate the average time per kilometer
    time_per_kilometer = total_time / total_distance

    # return the result in minutes per kilometer
    result = time_per_kilometer
    return result

print(solution())