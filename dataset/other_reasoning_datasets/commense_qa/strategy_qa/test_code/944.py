def solution():
    num_toes = 10 * 2
    num_marriages = 8
    if num_marriages <= num_toes:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())