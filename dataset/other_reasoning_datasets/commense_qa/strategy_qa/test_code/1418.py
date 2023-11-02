def solution():
    godfather_time_span = [1945, 1955]
    y2k_year = 2000
    if y2k_year in range(godfather_time_span[0], godfather_time_span[1]+1):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())