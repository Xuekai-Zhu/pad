def solution():
    """John adopts a dog from a shelter.  The dog ends up having health problems and this requires 3 vet appointments,  which cost $400 each.  After the first appointment, John paid $100 for pet insurance that covers 80% of the subsequent visits.  How much did he pay in total?"""
    # Define the cost of each vet appointment
    VET_COST = 400

    # Define the cost of pet insurance
    INSURANCE_COST = 100

    # Calculate the total cost of the first vet appointment
    total_cost = VET_COST

    # Calculate the cost of the subsequent vet appointments with insurance
    insurance_coverage = 0.8
    for i in range(1, 3):
        cost = (1 - insurance_coverage) * VET_COST
        total_cost += cost

    # Add the cost of the pet insurance
    total_cost += INSURANCE_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())