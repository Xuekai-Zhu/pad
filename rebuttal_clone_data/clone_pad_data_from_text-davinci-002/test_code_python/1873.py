def solution():
    sum_of_ages = 150
    Jeremy_age = 40
    Sebastian_age = Jeremy_age + 4
    Sophia_age = sum_of_ages - (Jeremy_age + Sebastian_age)
    Sophia_age_in_three_years = Sophia_age + 3
    result = Sophia_age_in_three_years
    return result

print(solution())