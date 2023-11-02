def solution():
    heart_failure_symptom = "red or pink legs"
    anorexia_nervosa_complication = "heart failure"
    if heart_failure_symptom in anorexia_nervosa_complication:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())