def solution():
    
    milk_per_day = 200
    days_in_june = 30
    milk_in_june = milk_per_day * days_in_june
    price_per_gallon = 3.55
    total_income = milk_in_june * price_per_gallon
    expenses = 3000
    net_income = total_income - expenses
    result = net_income
    return result

print(solution())