def solution():
    balding_years = ["before 2020"]
    hairline_change_years = ["2020"]
    overlap = [year for year in balding_years if year in hairline_change_years]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())