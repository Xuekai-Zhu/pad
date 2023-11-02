def solution():
    us_gdp_2018 = 20540000000000
    num_commas = len(str(us_gdp_2018)) // 3
    if num_commas <= 3:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())