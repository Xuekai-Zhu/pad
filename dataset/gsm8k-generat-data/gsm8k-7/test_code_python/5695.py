def solution():
    total_chips = 100
    ratio_ian = 4
    ratio_lyle = 6

    # Calculate the total number of parts in the ratio
    total_ratio_parts = ratio_ian + ratio_lyle

    # Calculate the number of parts that Lyle has
    lyle_parts = ratio_lyle / total_ratio_parts

    # Calculate the percentage of chips that Lyle has
    lyle_percentage = lyle_parts * 100

    result = lyle_percentage
    return result

print(solution())