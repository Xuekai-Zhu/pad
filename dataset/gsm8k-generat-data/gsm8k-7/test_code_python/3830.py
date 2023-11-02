def solution():
    disorder_prevalence = 0.25
    num_patients = 26 * 2  # twice the number of previous patients

    # Calculate the expected number of patients with ZYX syndrome
    expected_num_disordered = disorder_prevalence * num_patients
    result = expected_num_disordered
    return result

print(solution())