def solution():
    total_erasers = 35

    # Let's assume Gabriel collected x erasers
    # and Celine collected 2x erasers
    x = total_erasers / (1 + 2 + 4)
    celine_erasers = 2 * x
    result = celine_erasers
    return result

print(solution())