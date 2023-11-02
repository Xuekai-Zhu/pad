def solution():
    autumn_start = 9
    autumn_end = 12
    pearl_harbor_month = 12
    pearl_harbor_day = 7
    if pearl_harbor_month >= autumn_start and pearl_harbor_month <= autumn_end:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())