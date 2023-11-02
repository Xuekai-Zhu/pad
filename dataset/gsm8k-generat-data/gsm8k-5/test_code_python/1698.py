def solution():
    # Calculate the total number of clothes Cally washed
    cally_white_shirts = 10
    cally_colored_shirts = 5
    cally_shorts = 7
    cally_pants = 6
    total_cally_clothes = cally_white_shirts + cally_colored_shirts + cally_shorts + cally_pants

    # Calculate the total number of clothes Danny washed
    danny_white_shirts = 6
    danny_colored_shirts = 8
    danny_shorts = 10
    danny_pants = 6
    total_danny_clothes = danny_white_shirts + danny_colored_shirts + danny_shorts + danny_pants

    # Calculate the total number of clothes they washed together
    total_clothes = total_cally_clothes + total_danny_clothes
    result = total_clothes
    return result

print(solution())