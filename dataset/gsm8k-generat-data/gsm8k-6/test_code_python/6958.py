def solution():
    # Let's assume Alan handed out X tickets
    # Marcy handed out 6 less than 5 times as many tickets as Alan
    # So, Marcy handed out (5X - 6) tickets
    # Total number of tickets handed out is 150
    # So, X + (5X - 6) = 150
    # Solving for X:
    X = (150 + 6) / 6
    result = int(X)  # Alan handed out an integer number of tickets
    return result

print(solution())