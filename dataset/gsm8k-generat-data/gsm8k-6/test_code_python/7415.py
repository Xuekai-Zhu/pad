def solution():
    # Let x be the time in minutes to vacuum downstairs
    # Then the time to vacuum upstairs is (2x + 5)
    # The total time is x + (2x + 5) = 3x + 5 = 38
    # Solving for x, we get x = 11
    # Therefore, the time to vacuum upstairs is 2x + 5 = 2(11) + 5 = 27 minutes
    upstairs_time = 2*11 + 5
    result = upstairs_time
    return result

print(solution())