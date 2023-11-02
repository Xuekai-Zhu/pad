def solution():
    
    electricity_bill = 60
    gas_bill = 40
    gas_paid = gas_bill * 0.75 + 5
    water_bill = 40
    water_paid = water_bill * 0.5
    internet_bill = 25
    internet_paid = 4 * 5
    total_paid = electricity_bill + gas_paid + water_paid + internet_paid
    total_cost = electricity_bill + gas_bill + water_bill + internet_bill
    remaining_cost = total_cost - total_paid
    result = remaining_cost
    return result

print(solution())