def solution():
    """John adopts a dog from a shelter. The dog ends up having health problems and this requires 3 vet appointments, which cost $400 each. After the first appointment, John paid $100 for pet insurance that covers 80% of the subsequent visits. How much did he pay in total?"""
    num_appointments = 3
    cost_per_appointment = 400
    insurance_payment = 100
    uncovered_cost = cost_per_appointment - (cost_per_appointment * 0.8)
    total_cost = cost_per_appointment + (uncovered_cost * (num_appointments - 1)) - insurance_payment
    result = total_cost
    return result

print(solution())