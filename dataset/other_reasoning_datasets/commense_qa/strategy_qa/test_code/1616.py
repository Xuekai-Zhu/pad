def solution():
    start_year = 988
    end_year = 1700
    tsar_reign_start_year = 1530
    tsar_reign_end_year = 1585
    if tsar_reign_start_year >= start_year and tsar_reign_end_year <= end_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())