def solution():
    total_costs = 2000
    supplier_payment = 600
    debtor_payment = 800
    equipment_maintenance = 1200
    remaining_money = total_costs - supplier_payment - debtor_payment - equipment_maintenance
    result = remaining_money
    return result

print(solution())