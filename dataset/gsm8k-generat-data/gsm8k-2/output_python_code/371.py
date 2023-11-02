def solution():
    """TJ ran a 10K race last Saturday. He ran the first half in 20 minutes. He completed the second half in 30 minutes. What was his average time per kilometer?"""
    total_time = 20 + 30  # in minutes
    total_distance = 10  # in kilometers
    average_time_per_kilometer = total_time / total_distance
    result = average_time_per_kilometer
    return result

print(solution())