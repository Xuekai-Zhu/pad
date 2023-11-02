def solution():
    """Tom wants to visit Barbados. He needs to get 10 different vaccines to go and a doctor's visit. They each cost $45 and the doctor's visit costs $250 but insurance will cover 80% of these medical bills. The trip itself cost $1200. How much will he have to pay?"""
    # Define the cost of each vaccine
    vaccine_cost = 45

    # Define the number of vaccines needed
    num_vaccines = 10

    # Calculate the total cost of the vaccines
    total_vaccine_cost = vaccine_cost * num_vaccines

    # Define the cost of the doctor's visit
    doctor_visit_cost = 250

    # Calculate the cost of the doctor's visit after insurance coverage
    doctor_visit_cost_after_insurance = doctor_visit_cost * 0.2

    # Calculate the total cost of the medical bills after insurance coverage
    total_medical_cost = total_vaccine_cost + doctor_visit_cost_after_insurance

    # Define the cost of the trip
    trip_cost = 1200

    # Calculate the total cost
    total_cost = total_medical_cost + trip_cost

    # return the result
    result = total_cost
    return result

print(solution())