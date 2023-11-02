def solution():
    """Teresa is 59 and her husband Morio is 71 years old. Their daughter, Michiko was born when Morio was 38. How old was Teresa when she gave birth to Michiko?"""
    michiko_age_diff = 71 - 38
    teresa_age_diff = michiko_age_diff + 21 # Age difference between Teresa and Morio
    teresa_age = 59 - teresa_age_diff
    result = teresa_age
    return result

print(solution())