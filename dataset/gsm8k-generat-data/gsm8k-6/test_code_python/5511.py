def solution():
    nate_age = 14  # given Nate's age is 14
    ember_age = nate_age / 2  # Ember is half as old as Nate

    # Find the difference in years between when Ember is 14 and when Nate will be that age
    age_difference = nate_age - ember_age
    result = nate_age + age_difference
    return result

print(solution())