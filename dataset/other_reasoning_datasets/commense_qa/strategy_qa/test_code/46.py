def solution():
    history_of_mental_illness_disqualifies = True
    psychiatric_patients = True
    if not history_of_mental_illness_disqualifies and not psychiatric_patients:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())