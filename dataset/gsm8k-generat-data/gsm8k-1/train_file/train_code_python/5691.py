def solution():
    """Five years ago, the sum of Sebastian's age and his sister's age was 3/4 of their father's age. 
    How old is their father today if Sebastian is 40 years old and 10 years older than his sister?"""
    sebastian_age = 40
    sister_age = sebastian_age - 10
    father_age_5_years_ago = (sebastian_age - 5 + sister_age - 5) / (3/4)
    father_current_age = father_age_5_years_ago + 5*3 # adding 5 years for each person
    result = father_current_age
    return result

print(solution())