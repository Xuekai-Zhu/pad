def solution():
    # Calculate the cost of the three vet appointments before insurance
    vet_cost = 3 * 400

    # Calculate the cost of the second and third vet appointments after insurance
    insurance_cost = 2 * (0.2 * 400)  # Insurance covers 80% of the cost, so John pays 20% of the cost
    total_cost = vet_cost + insurance_cost + 100  # Add the cost of the first appointment and the insurance payment

    result = total_cost
    return result

print(solution())