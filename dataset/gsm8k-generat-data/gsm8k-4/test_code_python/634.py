def solution():
    """Vaishali has 4 hats, each with three stripes.  She also has three hats with four stripes each, six hats with no stripes, and another two hats with 5 stripes each.  What is the combined total number of stripes Vaishali has on all of her hats?"""
    # Calculate the total number of stripes on the hats with three stripes each
    three_stripes = 4 * 3

    # Calculate the total number of stripes on the hats with four stripes each
    four_stripes = 3 * 4

    # Calculate the total number of stripes on the hats with no stripes
    no_stripes = 6 * 0

    # Calculate the total number of stripes on the hats with five stripes each
    five_stripes = 2 * 5

    # Calculate the combined total number of stripes
    total_stripes = three_stripes + four_stripes + no_stripes + five_stripes

    # return the result
    result = total_stripes
    return result

print(solution())