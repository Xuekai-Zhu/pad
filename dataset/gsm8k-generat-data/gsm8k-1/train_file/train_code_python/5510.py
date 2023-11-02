def solution():
    """Ember is half as old as Nate who is 14. When she is 14 herself, how old will Nate be?"""
    nate_age = 14
    ember_age = nate_age / 2
    years_until_ember_is_14 = 14 - ember_age
    nate_age_at_ember_14 = nate_age + years_until_ember_is_14
    result = nate_age_at_ember_14
    return result

print(solution())