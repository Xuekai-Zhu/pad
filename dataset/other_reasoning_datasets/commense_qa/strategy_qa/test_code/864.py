def solution():
    u2_formed_year = 1976
    polo_grounds_demolished_year = 1964
    if u2_formed_year > polo_grounds_demolished_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())