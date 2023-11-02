def solution():
    """Teresa is 59 and her husband Morio is 71 years old. Their daughter, Michiko was born when Morio was 38. How old was Teresa when she gave birth to Michiko?"""
    age_difference = 71 - 38
    teresa_age_difference = age_difference + 21  # adding 21 to represent the age difference when Michiko was born
    teresa_age_at_michiko_birth = 59 - teresa_age_difference
    result = teresa_age_at_michiko_birth
    return result

print(solution())