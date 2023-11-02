def solution():
    monthly_charge = 30
    promotional_rate = monthly_charge / 3
    overage_charge = 15
    total_charge = promotional_rate + monthly_charge + monthly_charge + monthly_charge + overage_charge
    result = total_charge
    return result

print(solution())