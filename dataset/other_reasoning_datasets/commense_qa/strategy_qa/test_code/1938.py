def solution():
    high_school_class_birth_years = [1991, 1992, 1993]
    nixon_presidency_years = list(range(1969, 1974))
    overlap = [year for year in high_school_class_birth_years if year <= 1974 and year >= 1969]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())