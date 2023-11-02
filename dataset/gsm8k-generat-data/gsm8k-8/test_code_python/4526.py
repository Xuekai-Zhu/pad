def solution():
    # Calculate the total cost of the vaccinations and doctor's visit before insurance coverage
    medical_cost = 10 * 45 + 250

    # Calculate the amount covered by insurance
    insurance_coverage = 0.8 * medical_cost

    # Calculate the total cost of the medical expenses after insurance coverage
    total_medical_cost = medical_cost - insurance_coverage

    # Calculate the total cost of the trip
    trip_cost = 1200

    # Calculate the total cost of the trip including medical expenses
    total_cost = trip_cost + total_medical_cost

    # Return the amount Tom will have to pay
    result = total_cost
    return result

print(solution())