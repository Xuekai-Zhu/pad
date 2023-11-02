def solution():
    num_patients = 12
    std_care_patients = num_patients * 2 / 3  # assuming 2/3 of patients require standard care
    special_patients = num_patients / 3
    special_time_multiplier = 1.2  # 20% longer serving time for special dietary requirements
    serving_time_std = 5  # minutes per standard care patient

    # Calculate the total time to serve standard care patients
    serving_time_std_care = std_care_patients * serving_time_std

    # Calculate the total time to serve special patients
    serving_time_special = special_patients * serving_time_std * special_time_multiplier

    # Calculate the total serving time for all patients
    total_serving_time = serving_time_std_care + serving_time_special

    result = total_serving_time
    return result

print(solution())