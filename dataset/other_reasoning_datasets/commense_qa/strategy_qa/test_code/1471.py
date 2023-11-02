def solution():
    viscose_invented_year = 1892
    elizabeth_i_death_year = 1603
    if viscose_invented_year > elizabeth_i_death_year:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())