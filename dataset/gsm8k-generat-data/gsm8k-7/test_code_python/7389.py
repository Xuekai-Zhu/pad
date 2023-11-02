def solution():
    teresa_age = 59
    morio_age = 71
    morio_age_when_michiko_born = 38

    # Calculate the age difference between Morio and Teresa when Michiko was born
    age_difference = morio_age - teresa_age

    # Subtract the age difference from Morio's age when Michiko was born to get Teresa's age
    teresa_age_when_michiko_born = morio_age_when_michiko_born - age_difference
    result = teresa_age_when_michiko_born
    return result

print(solution())