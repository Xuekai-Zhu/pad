def solution():
     mri_cost = 1200
     doctor_hours = 0.5
     doctor_charge = 300 * doctor_hours
     visit_fee = 150
     insurance_coverage = 0.8
     total_cost = mri_cost + doctor_charge + visit_fee
     cost_after_insurance = total_cost * (1 - insurance_coverage)
     result = cost_after_insurance
     
     return result

print(solution())