def solution():
    # Calculate the number of patients likely to have ZYX syndrome
    total_patients = 26 * 2  # the clinic has doubled its previous number of 26 patients
    zyx_patients = total_patients // 4  # one in every four people has ZYX syndrome
    result = zyx_patients
    return result

print(solution())