def solution():
    joel_age = 5
    dad_age = 32
    age_diff = dad_age - joel_age

    dad_age_twice_joel_age = dad_age * 2

    years_to_double = dad_age_twice_joel_age - dad_age

    joel_age_when_doubled = joel_age + years_to_double
    result = joel_age_when_doubled
    return result

print(solution())