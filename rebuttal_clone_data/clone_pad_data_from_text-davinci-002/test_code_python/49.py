def solution():
    """On a school trip to the seashore, Alan and his friends collected shells. Alan collected four times as many shells as Ben did. Ben got a late start and only collected a third of what Laurie did. If Laurie collected 36 shells how many did Alan collect?"""
    Laurie_shells = 36
    Ben_shells = Laurie_shells / 3
    Alan_shells = Ben_shells * 4
    result = Alan_shells
    return result

print(solution())