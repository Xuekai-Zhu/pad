def solution():
    steven_falls = 3  # Steven fell down 3 times
    stephanie_falls = steven_falls + 13  # Stephanie fell down 13 more times than Steven
    sonya_falls = (stephanie_falls / 2) - 2  # Sonya fell down 2 times less than half the number of times Stephanie fell

    result = sonya_falls
    return result

print(solution())