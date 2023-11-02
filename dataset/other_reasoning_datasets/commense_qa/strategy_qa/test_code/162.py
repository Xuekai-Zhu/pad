def solution():
    golden_age_start = 1930
    golden_age_end = 1950
    shatter_pub_year = 1985
    if shatter_pub_year > golden_age_end:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())