def solution():
    initial_temp = 40
    double_temp = initial_temp * 2
    reduce_temp = double_temp - 30
    reduce_percent_temp = reduce_temp * 0.7
    increase_temp = reduce_percent_temp + 24
    result = increase_temp
    return result

print(solution())