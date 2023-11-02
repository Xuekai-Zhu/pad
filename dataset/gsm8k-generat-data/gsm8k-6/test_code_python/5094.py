def solution():
    # Calculate the cost of medication
    medication_cost = 0.5 * 5000  

    # Calculate the remaining bill after medication cost
    remaining_bill = 5000 - medication_cost

    # Calculate the cost of overnight stays
    overnight_stays_cost = 0.25 * remaining_bill

    # Calculate the cost of ambulance ride
    ambulance_cost = remaining_bill - overnight_stays_cost - 175

    result = ambulance_cost
    return result

print(solution())