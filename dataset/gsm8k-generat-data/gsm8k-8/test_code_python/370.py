def solution():
    # Calculate the number of patients requiring special dietary requirements
    special_care_patients = 12 / 3

    # Calculate the increased serving time for special care patients
    special_care_time = 5 * 1.2

    # Calculate the total serving time for all patients
    total_serving_time = (12 - special_care_patients) * 5 + special_care_patients * special_care_time

    # Convert the serving time to minutes and return the result
    result = total_serving_time
    return result

print(solution())