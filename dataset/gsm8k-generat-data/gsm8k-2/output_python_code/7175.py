def solution():
    """Tate finishes high school in 1 year less than normal. It takes him 3 times that long to get his bachelor's degree and Ph.D. How many years did he spend in high school and college?"""
    normal_hs_time = 4
    tate_hs_time = normal_hs_time - 1
    college_time = 3 * normal_hs_time
    total_time = tate_hs_time + college_time
    result = total_time
    return result

print(solution())