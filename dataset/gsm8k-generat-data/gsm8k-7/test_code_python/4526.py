def solution():
    num_vaccines = 10
    vaccine_cost = 45
    doctor_visit_cost = 250
    insurance_cover = 0.8
    trip_cost = 1200

    # Calculate the total cost of all vaccines
    total_vaccine_cost = num_vaccines * vaccine_cost

    # Calculate the total cost of the doctor's visit
    total_doctor_visit_cost = doctor_visit_cost * insurance_cover

    # Calculate the total cost of all medical bills
    total_medical_bills = total_vaccine_cost + total_doctor_visit_cost

    # Calculate the total cost of the trip
    total_cost = total_medical_bills + trip_cost
    result = total_cost
    return result

print(solution())