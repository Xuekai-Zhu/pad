def solution():
    """CJ, KJ, and AJ collect stamps.  CJ has 5 more than twice the number of stamps that KJ has, and KJ has half as many as AJ.  If the three boys have 930 stamps all together, how many stamps does AJ have?"""
    # Let x be the number of stamps AJ has
    x = 2 * 5 + 5  # CJ has 5 more than twice KJ's stamps, and KJ has half as many as AJ
    y = x / 2  # KJ has half as many stamps as AJ
    z = x + y + 5  # The three boys have 930 stamps in total

    # solve for x
    x = (930 - y - z) / 1.5

    # Display the number of stamps AJ has
    result = x
    return result

print(solution())