def solution():
    """Steven, Stephanie, and Sonya went ice skating. Steven only fell down 3 times, but Stephanie had 13 more falls than Steven. If Sonya fell down 2 times less than half the number of times Stephanie fell, how many times did Sonya fall?"""
    # Define the number of times Steven fell
    steven_falls = 3

    # Calculate the number of times Stephanie fell
    stephanie_falls = steven_falls + 13

    # Calculate half the number of times Stephanie fell
    half_stephanie_falls = stephanie_falls / 2

    # Calculate the number of times Sonya fell
    sonya_falls = half_stephanie_falls - 2

    # return the result
    result = sonya_falls
    return result

print(solution())