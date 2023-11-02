def solution():
    # Let's assume Gabriel collected x erasers
    # Then Celine collected 2x erasers, and Julian collected 4x erasers
    total_erasers = 35  # total number of erasers collected
    x = total_erasers/10  # dividing by 10 to simplify the calculation
    celine_erasers = 2*x  # number of erasers collected by Celine

    result = celine_erasers
    return result

print(solution())