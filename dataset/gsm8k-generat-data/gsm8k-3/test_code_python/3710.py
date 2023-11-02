def solution():
    """4 students participated in a 200m race. If the average completion time of the last three students was 35 seconds, and the average completion time of all four runners was 30 seconds, how long (in seconds) did it take the student who came first to finish the race?"""
    # Let x be the completion time of the first student
    # Then we have:
    # (x + 35 + 35 + 35)/4 = 30  (average completion time of all four runners)
    # x + 105 = 120
    # x = 15

    # Therefore, the first student completed the race in 15 seconds
    result = 15
    return result

print(solution())