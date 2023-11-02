def solution():
    # Define the jumps of the three next highest jumpers
    jumps = [23, 27, 28]

    # Calculate the average jump
    avg_jump = sum(jumps) / len(jumps)

    # Calculate Ravi's jump
    ravi_jump = 1.5 * avg_jump

    result = ravi_jump
    return result

print(solution())