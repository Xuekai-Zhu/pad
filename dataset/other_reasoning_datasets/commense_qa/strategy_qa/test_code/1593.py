def solution():
    inauguration_year = 1961
    founding_year = 1985
    if founding_year > inauguration_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())