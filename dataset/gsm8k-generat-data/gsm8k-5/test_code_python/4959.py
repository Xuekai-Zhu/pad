def solution():
    # Number of multiple-choice questions already written
    mc_written = 2/5 * 35

    # Number of problem-solving questions already written
    ps_written = 1/3 * 15

    # Total number of questions already written
    total_written = mc_written + ps_written

    # Number of remaining questions to write
    remaining = 35 + 15 - total_written
    result = remaining
    return result

print(solution())