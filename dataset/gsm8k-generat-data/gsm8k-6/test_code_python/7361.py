def solution():
    # Calculate the total number of patients John treats at both hospitals in a week
    first_hospital_patients = 20
    second_hospital_patients = 1.20 * first_hospital_patients  # 20% more than the first hospital
    weekly_patients = first_hospital_patients + second_hospital_patients

    # Calculate the total number of patients John treats in 50 weeks
    total_patients = weekly_patients * 5 * 50
    result = total_patients
    return result

print(solution())