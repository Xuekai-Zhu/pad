def solution():
    """Steven, Stephanie, and Sonya went ice skating. Steven only fell down 3 times, but Stephanie had 13 more falls than Steven. If Sonya fell down 2 times less than half the number of times Stephanie fell, how many times did Sonya fall?"""
    steven_falls = 3
    stephanie_falls = steven_falls + 13
    sonya_falls = (stephanie_falls / 2) - 2
    result = sonya_falls
    return result

print(solution())