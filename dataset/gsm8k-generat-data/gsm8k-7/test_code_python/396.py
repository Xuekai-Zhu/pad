def solution():
    insulin_pills_per_day = 2
    blood_pressure_pills_per_day = 3
    anticonvulsants_per_day = 2 * blood_pressure_pills_per_day
    num_days_in_week = 7

    # Calculate the total number of insulin pills Holly takes in a week
    total_insulin_pills = insulin_pills_per_day * num_days_in_week

    # Calculate the total number of blood pressure pills Holly takes in a week
    total_blood_pressure_pills = blood_pressure_pills_per_day * num_days_in_week

    # Calculate the total number of anticonvulsant pills Holly takes in a week
    total_anticonvulsants = anticonvulsants_per_day * num_days_in_week

    # Calculate the total number of pills Holly takes in a week
    total_pills = total_insulin_pills + total_blood_pressure_pills + total_anticonvulsants
    result = total_pills
    return result

print(solution())