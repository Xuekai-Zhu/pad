def solution():
    pounds_trout = 200
    pounds_salmon = pounds_trout + (pounds_trout / 2)
    pounds_tuna = pounds_trout * 2
    total_pounds = pounds_trout + pounds_salmon + pounds_tuna
    result = total_pounds
    return result

print(solution())