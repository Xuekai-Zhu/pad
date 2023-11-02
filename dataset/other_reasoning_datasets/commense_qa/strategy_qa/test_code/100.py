def solution():
    apollo_13_casualties = 0
    challenger_casualties = 7
    columbia_casualties = 7
    if apollo_13_casualties < (challenger_casualties + columbia_casualties):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())