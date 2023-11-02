def solution():
    german_shepherd_min_height = 22
    german_shepherd_max_height = 26
    robert_wadlow_height = 8*12 + 11.1 #inches
    if robert_wadlow_height > german_shepherd_max_height:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())