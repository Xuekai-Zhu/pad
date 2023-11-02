def solution():
    average_peas_per_pod = 6.5
    billion_commas = 3
    if average_peas_per_pod >= billion_commas:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())