def solution():
    """When Hannah was 6 years old, her age was double the age of her sister July. Now, 20 years later, if July's husband is 2 years older than her, how old is he?"""
    hannah_current_age = 6 + 20
    july_current_age = hannah_current_age / 2
    july_husband_age = july_current_age + 2
    result = july_husband_age
    return result

print(solution())