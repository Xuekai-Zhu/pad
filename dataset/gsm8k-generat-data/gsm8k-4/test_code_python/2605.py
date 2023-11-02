def solution():
    """John adopts a dog from a shelter. The dog ends up having health problems and this requires 3 vet appointments, which cost $400 each. After the first appointment, John paid $100 for pet insurance that covers 80% of the subsequent visits. How much did he pay in total?"""
    # Define the cost of each vet appointment
    VET_COST = 400

    # Define the cost of the first vet appointment
    first_appointment_cost = VET_COST

    # Define the cost of the remaining vet appointments after taking into account the pet insurance coverage
    remaining_appointment_cost = VET_COST * 0.2

    # Calculate the total cost of the vet appointments, including the cost of the pet insurance
    total_cost = (first_appointment_cost + (2 * remaining_appointment_cost)) + 100

    result = total_cost
    return result

print(solution())