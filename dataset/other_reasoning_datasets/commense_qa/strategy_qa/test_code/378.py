def solution():
    methane_gas = True
    colorless = True
    odorless = True
    if methane_gas and colorless and odorless:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())