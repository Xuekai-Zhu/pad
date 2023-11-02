def solution():
    thirty_years = 30
    cockatoo_lifespan = range(40, 61)
    if max(cockatoo_lifespan) >= thirty_years:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())