def solution():
    # Determine the number of patients John sees each day at the second hospital
    second_hospital_patients = 20 * 1.2

    # Determine the total number of patients John sees each day
    total_patients = 20 + second_hospital_patients

    # Determine the total number of patients John sees in a week
    weekly_patients = total_patients * 5

    # Determine the total number of patients John treats in a year
    yearly_patients = weekly_patients * 50

    result = yearly_patients
    return result

print(solution())