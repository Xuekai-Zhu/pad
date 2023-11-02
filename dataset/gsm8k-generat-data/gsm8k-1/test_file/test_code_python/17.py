def solution():
    """Raymond and Samantha are cousins. Raymond was born 6 years before Samantha. Raymond had a son at the age of 23. If Samantha is now 31, how many years ago was Raymond's son born?"""
    age_difference = 6
    raymond_age = 31 + age_difference
    when_son_born = 23
    years_ago_son_born = raymond_age - when_son_born
    result = years_ago_son_born
    return result

print(solution())