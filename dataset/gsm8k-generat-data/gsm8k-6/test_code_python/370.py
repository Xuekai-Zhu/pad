def solution():
    # Calculate the number of patients with special dietary requirements
    special_patients = 12 / 3

    # Calculate the total serving time for all patients
    total_serving_time = (9 * 5) + (special_patients * (5 * 1.2)) # 9 patients require standard care, special patients take 20% longer

    result = total_serving_time
    return result

print(solution())