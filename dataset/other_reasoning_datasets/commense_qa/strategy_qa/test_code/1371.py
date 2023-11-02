def solution():
    plague_cases = 7
    selfie_deaths = 259
    if selfie_deaths > plague_cases:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())