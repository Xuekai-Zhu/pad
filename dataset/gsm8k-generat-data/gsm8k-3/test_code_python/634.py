def solution():
    """Vaishali has 4 hats, each with three stripes.  She also has three hats with four stripes each, six hats with no stripes, and another two hats with 5 stripes each.  What is the combined total number of stripes Vaishali has on all of her hats?"""
    # Define the number of stripes on each type of hat
    HAT1_STRIPES = 3
    HAT2_STRIPES = 4
    HAT3_STRIPES = 0
    HAT4_STRIPES = 5

    # Define the number of each type of hat
    hat1 = 4
    hat2 = 3
    hat3 = 6
    hat4 = 2

    # Calculate the total number of stripes
    total_stripes = (hat1 * HAT1_STRIPES) + (hat2 * HAT2_STRIPES) + (hat3 * HAT3_STRIPES) + (hat4 * HAT4_STRIPES)

    # Display the total number of stripes
    result = total_stripes
    return result

print(solution())