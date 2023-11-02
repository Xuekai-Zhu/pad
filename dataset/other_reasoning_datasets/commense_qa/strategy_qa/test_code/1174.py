def solution():
    pitman_invented_year = 1837
    tenth_amendment_year = 1791
    if tenth_amendment_year < pitman_invented_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())