def solution():
    """Together, Alan and Marcy handed out 150 parking tickets. If Marcy handed out 6 fewer than 5 times as many tickets as Alan, how many tickets did Alan hand out?"""
    # Let x be the number of tickets Alan handed out
    x = 0

    # Marcy handed out 6 fewer than 5 times as many tickets as Alan
    y = 5 * x - 6

    # The total number of tickets is 150
    x + y = 150

    # Solve for x to find how many tickets Alan handed out
    x = (150 + 6) / 6

    # Display the number of tickets Alan handed out
    result = x
    return result

print(solution())