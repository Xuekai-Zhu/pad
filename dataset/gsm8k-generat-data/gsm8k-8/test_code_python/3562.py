def solution():
    # Set up the equations
    # cj = 2kj + 5 and kj = 0.5aj
    # cj + kj + aj = 930

    # Substitute kj in terms of aj into the first equation
    # cj = 2(0.5aj) + 5
    # cj = aj + 5

    # Substitute the expression for cj into the second equation
    # aj + 5 + kj + aj = 930
    # 2aj + kj = 925
    # Substitute kj in terms of aj
    # 2aj + 0.5aj = 925
    # 2.5aj = 925
    # aj = 370 stamps

    aj_stamps = 370
    result = aj_stamps
    return result

print(solution())