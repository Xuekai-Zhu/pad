def solution():
    # Calculate the average jump of the three next highest jumpers
    avg_jump = (23 + 27 + 28) / 3

    # Calculate how high Ravi can jump
    ravi_jump = avg_jump * 1.5

    result = ravi_jump
    return result

print(solution())