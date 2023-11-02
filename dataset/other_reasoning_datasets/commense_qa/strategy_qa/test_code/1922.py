def solution():
    beethoven_death_year = 1827
    edm_origin_year = 1950
    if beethoven_death_year < edm_origin_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())