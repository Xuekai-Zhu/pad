def solution():
    """CJ, KJ, and AJ collect stamps. CJ has 5 more than twice the number of stamps that KJ has, and KJ has half as many as AJ. If the three boys have 930 stamps all together, how many stamps does AJ have?"""
    # Let x be the number of stamps that AJ has
    x = None

    # Calculate the number of stamps that KJ has
    kj_stamps = x / 2

    # Calculate the number of stamps that CJ has
    cj_stamps = 2 * kj_stamps + 5

    # Calculate the total number of stamps that the three boys have
    total_stamps = x + kj_stamps + cj_stamps

    # Solve for x
    x = (930 - 5 - 2 * kj_stamps - kj_stamps) / 2

    # Return the result
    result = x
    return result

print(solution())