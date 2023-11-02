def solution():
    jen_flips = 16  # Jen did 16 triple-flips
    tyler_flips = jen_flips * 3 / 2  # Tyler did half as many flips as Jen, and each of Jen's flips was three flips
    double_flips = tyler_flips / 2  # Tyler was practicing double-flips

    result = double_flips
    return result

print(solution())