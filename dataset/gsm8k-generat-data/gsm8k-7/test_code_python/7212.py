def solution():
    jumper1 = 23
    jumper2 = 27
    jumper3 = 28

    # Calculate the average jump of the three next highest jumpers
    avg_jump = (jumper1 + jumper2 + jumper3) / 3

    # Calculate Ravi's jump height
    ravi_jump = avg_jump * 1.5
    result = ravi_jump
    return result

print(solution())