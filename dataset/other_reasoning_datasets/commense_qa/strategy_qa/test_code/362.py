def solution():
    pyramid_base_length = 756
    man_height = 5.75 # 5 feet 9 inches
    num_men_needed = pyramid_base_length / man_height
    if num_men_needed >= 200:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())