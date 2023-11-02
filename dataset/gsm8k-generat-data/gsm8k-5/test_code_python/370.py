def solution():
    num_standard_care = 12 * (2 / 3)  # 2/3 of the patients require standard care
    num_special_care = 12 * (1 / 3)  # 1/3 of the patients have special dietary requirements
    serving_time_special = 1.2 * 5  # Special care patients have a 20% longer serving time
    serving_time_standard = 5  # Standard care patients take 5 minutes to serve

    # Calculate the total serving time for all patients
    total_serving_time = (num_standard_care * serving_time_standard) + (num_special_care * serving_time_special)
    result = total_serving_time
    return result

print(solution())