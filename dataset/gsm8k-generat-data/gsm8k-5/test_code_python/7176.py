def solution():
    normal_time_hs = 4  # Normal time to finish high school is 4 years
    time_hs = normal_time_hs - 1  # Tate finishes high school in 1 year less than normal
    time_college = 3 * (normal_time_hs + time_hs)  # Tate takes 3 times the time he spent in high school and bachelor's to get his Ph.D.

    # Calculate the total time Tate spends in high school and college
    total_time = time_hs + time_college
    result = total_time
    return result

print(solution())