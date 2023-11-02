def solution():
    # Define the percentage of people with ZYX syndrome
    zyx_percentage = 0.25

    # Calculate the number of patients likely to have ZYX syndrome
    total_patients = 26 * 2
    zyx_patients = zyx_percentage * total_patients

    result = zyx_patients
    return result

print(solution())