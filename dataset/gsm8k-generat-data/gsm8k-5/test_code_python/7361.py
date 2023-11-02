def solution():
    patients_per_day1 = 20  # John sees 20 patients each day at hospital 1
    patients_per_day2 = patients_per_day1 * 1.2  # John sees 20% more patients each day at hospital 2
    days_per_week = 5  # John works 5 days a week
    weeks = 50  # John works 50 weeks per year

    # Calculate the total number of patients John treats in a year
    total_patients = (patients_per_day1 + patients_per_day2) * days_per_week * weeks
    result = total_patients
    return result

print(solution())