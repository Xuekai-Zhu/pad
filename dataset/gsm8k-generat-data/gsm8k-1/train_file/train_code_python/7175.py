def solution():
    """Tate finishes high school in 1 year less than normal. It takes him 3 times that long to get his bachelor's degree and Ph.D. How many years did he spend in high school and college?"""
    high_school_duration = 4 - 1 # 1 year less than normal
    college_duration = 3 * high_school_duration
    total_duration = high_school_duration + college_duration
    result = total_duration
    return result

print(solution())