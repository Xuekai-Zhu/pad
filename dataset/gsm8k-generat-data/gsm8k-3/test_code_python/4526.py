def solution():
    """Tom wants to visit Barbados.  He needs to get 10 different vaccines to go and a doctor's visit.  They each cost $45 and the doctor's visit costs $250 but insurance will cover 80% of these medical bills.  The trip itself cost $1200.  How much will he have to pay?"""
    # Define the cost of each vaccine and the doctor's visit before insurance
    VACCINE_COST = 45
    DOCTOR_VISIT_COST = 250

    # Calculate the total cost of the vaccines
    vaccine_cost = VACCINE_COST * 10

    # Calculate the total cost of the doctor's visit
    doctor_visit_cost = DOCTOR_VISIT_COST

    # Calculate the total cost of all medical expenses before insurance
    total_medical_cost = vaccine_cost + doctor_visit_cost

    # Calculate the 80% insurance coverage on the medical expenses
    insurance_coverage = total_medical_cost * 0.8

    # Calculate the total cost of all medical expenses after insurance
    total_medical_cost_after_insurance = total_medical_cost - insurance_coverage

    # Calculate the total cost of the trip
    total_trip_cost = total_medical_cost_after_insurance + 1200

    # Display the total cost that Tom will have to pay
    result = total_trip_cost
    return result

print(solution())