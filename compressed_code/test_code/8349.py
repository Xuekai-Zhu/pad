def solution():
    
    property_damage = 40000
    medical_bills = 70000
    insurance_coverage = 0.8
    personal_coverage = 0.2
    total_cost = property_damage + medical_bills
    insurance_pay = total_cost * insurance_coverage
    personal_pay = total_cost * personal_coverage
    result = personal_pay
    return result

print(solution())