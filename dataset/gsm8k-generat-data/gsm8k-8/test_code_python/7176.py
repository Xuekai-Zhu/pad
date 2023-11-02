def solution():
    normal_hs_duration = 4 # normal high school duration is 4 years
    hs_duration = normal_hs_duration - 1 # Tate finishes high school in 1 year less than normal
    college_duration = 3 * hs_duration # it takes 3 times the duration of high school to get bachelor's and Ph.D.

    # Calculate the total duration of high school and college
    total_duration = hs_duration + college_duration
    result = total_duration
    return result

print(solution())