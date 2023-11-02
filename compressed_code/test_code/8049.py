def solution():
    
    monthly_income = 2000
    transport_fare_percentage = 5
    transport_fare = (transport_fare_percentage / 100) * monthly_income
    remaining_income = monthly_income - transport_fare
    result = remaining_income
    return result

print(solution())