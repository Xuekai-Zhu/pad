def solution():
    boeing_737_cost = 1.6 * 10**6
    wonder_woman_gross = 800 * 10**6
    if wonder_woman_gross > boeing_737_cost:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())