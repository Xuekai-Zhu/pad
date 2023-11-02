def solution():
    # Calculate the total cost of the vet appointments
    total_cost = 3 * 400  # 3 vet appointments at $400 each

    # Calculate the remaining cost after pet insurance coverage
    remaining_cost = total_cost - (400 - 0.8*400) - (400 - 0.8*400)

    # Add the cost of the first appointment and the remaining cost
    total_paid = remaining_cost + 100  # John paid $100 for the pet insurance

    result = total_paid
    return result

print(solution())