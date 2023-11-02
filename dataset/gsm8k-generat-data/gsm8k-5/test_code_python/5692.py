def solution():
    sebastian_age = 40  # Sebastian is 40 years old
    sister_age = sebastian_age - 10  # Sebastian's sister is 10 years younger than him
    father_age_5_years_ago = (sebastian_age + sister_age) / (3/4)  # Five years ago, the sum of their ages was 3/4 of their father's age
    father_age_today = father_age_5_years_ago + 5  # Add 5 years to get their father's current age
    result = father_age_today
    return result

print(solution())