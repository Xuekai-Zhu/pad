def solution():
    """John's pool is 5 feet deeper than 2 times Sarah’s pool. If John’s pool is 15 feet deep, how deep is Sarah’s pool?"""
    # Define John's pool depth and the equation relating it to Sarah's pool depth
    john_depth = 15
    equation = john_depth - 5 == 2 * sarah_depth

    # Solve for Sarah's pool depth
    sarah_depth = (john_depth - 5) / 2

    # Return the result
    result = sarah_depth
    return result

print(solution())