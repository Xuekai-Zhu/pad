def solution():
    has_leukophobia = True
    color_of_us_flag = ["red", "white", "blue"]
    if "white" in color_of_us_flag and has_leukophobia:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())