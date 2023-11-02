def solution():
    bipolar_prevalence = 0.01
    diabetes_prevalence = 0.1
    if bipolar_prevalence > diabetes_prevalence:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())