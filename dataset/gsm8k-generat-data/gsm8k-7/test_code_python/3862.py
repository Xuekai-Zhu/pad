def solution():
    adult_patients_per_hour = 4
    child_patients_per_hour = 3
    hours_per_day = 8
    adult_visit_cost = 50
    child_visit_cost = 25

    # Calculate the total number of adult patients seen in a day
    total_adult_patients = adult_patients_per_hour * hours_per_day

    # Calculate the total number of child patients seen in a day
    total_child_patients = child_patients_per_hour * hours_per_day

    # Calculate the total amount earned from adult patients
    total_adult_earned = total_adult_patients * adult_visit_cost

    # Calculate the total amount earned from child patients
    total_child_earned = total_child_patients * child_visit_cost

    # Calculate the total earned for seeing all patients
    total_earned = total_adult_earned + total_child_earned
    result = total_earned
    return result

print(solution())