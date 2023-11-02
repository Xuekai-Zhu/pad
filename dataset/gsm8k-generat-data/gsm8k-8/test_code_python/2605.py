def solution():
    # Calculate the cost of the three vet appointments before insurance
    vet_cost = 3 * 400
    # Calculate the cost of the second and third appointments after insurance
    after_insurance = 2 * (0.2 * 400)
    # Calculate the total cost including insurance
    total_cost = vet_cost + after_insurance - 100
    result = total_cost
    return result

print(solution())