def solution():
    initial_temp = 40  # initial temperature is 40 degrees
    double_temp = 2 * initial_temp  # double the initial temperature
    dad_temp = double_temp - 30  # reduce the temperature by 30 degrees
    mom_temp = dad_temp - (0.3 * dad_temp)  # reduce the temperature by 30%
    sister_temp = mom_temp + 24  # increase the temperature by 24 degrees

    result = sister_temp
    return result

print(solution())