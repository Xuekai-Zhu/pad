def solution():
    """On a school trip to the seashore, Alan and his friends collected shells. Alan collected four times as many shells as Ben did. Ben got a late start and only collected a third of what Laurie did. If Laurie collected 36 shells, how many did Alan collect?"""
    laurie_shells = 36
    ben_shells = laurie_shells / 3
    alan_shells = 4 * ben_shells
    result = alan_shells
    return result

print(solution())