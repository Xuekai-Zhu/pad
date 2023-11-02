def solution():
    present1 = 2  # square feet
    present2 = present1 * 0.75  # three-quarters of present1
    present3 = (present1 + present2) * 2  # same amount as both other presents put together

    total_wrapping_paper = present1 + present2 + present3
    result = total_wrapping_paper
    return result

print(solution())