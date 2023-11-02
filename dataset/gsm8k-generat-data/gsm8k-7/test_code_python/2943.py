def solution():
    initial_temp = 40
    temp_after_jerry = initial_temp * 2
    temp_after_dad = temp_after_jerry - 30
    temp_after_mom = temp_after_dad * 0.7
    temp_after_sister = temp_after_mom + 24
    result = temp_after_sister
    return result

print(solution())