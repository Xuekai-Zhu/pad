def solution():
    spice_girls_formed_year = 1994
    spice_girls_active_range = range(1990, 2000)
    little_mix_formed_year = 2011
    if spice_girls_formed_year < little_mix_formed_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())