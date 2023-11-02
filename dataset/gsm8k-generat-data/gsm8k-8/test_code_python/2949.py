def solution():
    # Calculate the total time used by the family in the bathroom
    total_bathroom_time = 45 + 30 + 20

    # Calculate the time left for Mrs. Parker to use the bathroom
    time_left = 2.5 + 2 - (total_bathroom_time / 60) - 5

    result = time_left
    return result

print(solution())