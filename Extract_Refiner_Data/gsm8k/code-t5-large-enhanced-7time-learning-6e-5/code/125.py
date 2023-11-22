def solution():
    
    # Define the number of patients seen per day and the average patient lifetime in minutes
    patients_per_day = 500
    patient_lifetime = 24

    # Calculate the total time spent on patients per day
    total_patients_time = patients_per_day * patient_lifetime

    # Calculate the total cost of the doctors
    doctors_cost = total_patients_time * 150

    # Calculate the total cost of the hospital's patients
    hospital_patients_cost = total_patients_time * 200

    # Calculate the profit
    profit = hospital_patients_cost - doctors_cost

    # return the result
    result = profit
    return result

print(solution())