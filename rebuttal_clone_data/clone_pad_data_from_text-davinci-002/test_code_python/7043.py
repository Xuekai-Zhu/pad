def solution():
    electricity = 60
    gas = 40
    water = 40
    internet = 25
    
    electricity_paid = electricity
    gas_paid = (gas * 3) / 4
    gas_payment = 5
    water_paid = water / 2
    internet_paid = (internet * 4) / 5
    
    total_paid = electricity_paid + gas_paid + gas_payment + water_paid + internet_paid
    total_bill = electricity + gas + water + internet
    
    result = total_bill - total_paid
    
    return result

print(solution())