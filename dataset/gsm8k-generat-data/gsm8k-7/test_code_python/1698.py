def solution():
    cally_white_shirts = 10
    cally_colored_shirts = 5
    cally_shorts = 7
    cally_pants = 6

    danny_white_shirts = 6
    danny_colored_shirts = 8
    danny_shorts = 10
    danny_pants = 6

    # Calculate the total number of clothes that Cally washed
    cally_total_clothes = cally_white_shirts + cally_colored_shirts + cally_shorts + cally_pants

    # Calculate the total number of clothes that Danny washed
    danny_total_clothes = danny_white_shirts + danny_colored_shirts + danny_shorts + danny_pants

    # Calculate the total number of clothes that they both washed
    total_clothes = cally_total_clothes + danny_total_clothes
    result = total_clothes
    return result

print(solution())