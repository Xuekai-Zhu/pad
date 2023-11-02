def solution():
    data_total = 500
    data_used = 300 + (2/5 * (data_total - 300))
    data_left = data_total - data_used
    result = data_left 
    return result

print(solution())