def solution():
    """When Hannah was 6 years old, her age was double the age of her sister July. Now, 20 years later, if July's husband is 2 years older than her, how old is he?"""
    hannah_age = 6
    july_age = hannah_age / 2
    july_current_age = july_age + 20
    husband_age = july_current_age + 2
    result = husband_age
    return result

print(solution())