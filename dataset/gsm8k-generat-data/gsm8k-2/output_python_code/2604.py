def solution():
    """John adopts a dog from a shelter. The dog ends up having health problems and this requires 3 vet appointments, which cost $400 each. After the first appointment, John paid $100 for pet insurance that covers 80% of the subsequent visits. How much did he pay in total?"""
    total_appointments = 3
    appointment_cost = 400
    insurance_cost = 100
    insurance_coverage = 0.8
    total_cost = 0
    for i in range(total_appointments):
        if i == 0:
            total_cost += appointment_cost
        else:
            total_cost += (1-insurance_coverage) * appointment_cost
    total_cost -= insurance_cost
    result = total_cost
    return result

print(solution())