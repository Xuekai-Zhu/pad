def solution():
    """Mia and Emma are currently 16 years apart in age. If Mia, who is younger than Emma, is 40 years old, what's the average of their ages?"""
    mia_age = 40
    emma_age = mia_age + 16
    age_sum = mia_age + emma_age
    average_age = age_sum / 2
    result = average_age
    return result

print(solution())