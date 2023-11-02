def solution():
    pittsburgh_acceptance_rate = 0.6
    fbi_acceptance_rate = 900/16000
    if pittsburgh_acceptance_rate > fbi_acceptance_rate:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())