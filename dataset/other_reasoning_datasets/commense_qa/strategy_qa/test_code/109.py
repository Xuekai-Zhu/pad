def solution():
    amendment_year = 1961
    truman_years = [1945, 1953]
    if amendment_year < truman_years[0] or amendment_year > truman_years[1]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())