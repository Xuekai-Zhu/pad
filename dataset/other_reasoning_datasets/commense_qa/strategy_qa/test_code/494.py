def solution():
    breakdancing_created_year = 1970
    ww2_years = list(range(1939, 1946))
    if breakdancing_created_year not in ww2_years:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())