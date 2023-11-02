def solution():
    """On a school trip to the seashore, Alan and his friends collected shells. Alan collected four times as many shells as Ben did. Ben got a late start and only collected a third of what Laurie did. If Laurie collected 36 shells how many did Alan collect?"""
    # Define the number of shells Laurie collected
    laurie_shells = 36

    # Calculate the number of shells Ben collected
    ben_shells = laurie_shells / 3

    # Calculate the number of shells Alan collected
    alan_shells = ben_shells * 4

    result = alan_shells
    return result

print(solution())