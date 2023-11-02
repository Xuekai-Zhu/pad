def solution():
    dopamine_consumption = "endogenous"
    if dopamine_consumption != "exogenous":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())