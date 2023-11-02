def solution():
     vet_appointments = 3
     appointment_cost = 400
     initial_payment = 100
     insurance_coverage = 0.8
     total_cost = (vet_appointments * appointment_cost) - (initial_payment * insurance_coverage)
     result = total_cost
     return result

print(solution())