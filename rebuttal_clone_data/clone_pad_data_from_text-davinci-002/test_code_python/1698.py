def solution():
    cally_white_shirts = 10
    cally_colored_shirts = 5
    cally_shorts = 7
    cally_pants = 6
    danny_white_shirts = 6
    danny_colored_shirts = 8
    danny_shorts = 10
    danny_pants = 6
    total_shirts = cally_white_shirts + cally_colored_shirts + danny_white_shirts + danny_colored_shirts
    total_pants = cally_pants + danny_pants
    total_clothes = total_shirts + total_pants
    result = total_clothes
    return result

print(solution())