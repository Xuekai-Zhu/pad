def solution():
    # Define the events in Dr. Seuss's life
    wife_suicide = True
    cancer_diagnosis = True
    # Check if he lived a tragedy free life
    if wife_suicide or cancer_diagnosis:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())