def solution():
    patients_per_day_first_hospital = 20
    additional_patients_percent = 20
    patients_per_day_second_hospital = patients_per_day_first_hospital * (1 + additional_patients_percent/100)
    days_per_week = 5
    weeks_per_year = 50

    # Calculate the total number of patients John treats each week
    total_patients_per_week = patients_per_day_first_hospital + patients_per_day_second_hospital

    # Calculate the total number of patients John treats each year
    total_patients_per_year = total_patients_per_week * days_per_week * weeks_per_year

    result = total_patients_per_year
    return result

print(solution())