def solution():
    
    property_damage = 40000
    medical_bills = 70000
    insurance_coverage = 0.8
    carl_share = 0.2
    total_cost = property_damage + medical_bills
    carl_owes = total_cost * carl_share
    result = carl_owes
    return result

print(solution())