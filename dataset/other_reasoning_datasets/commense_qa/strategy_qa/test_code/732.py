def solution():
    washington_monument_opened = 1888
    sojourner_truth_died = 1883
    if sojourner_truth_died < washington_monument_opened:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())