def solution():
    
    house_cost = 480000
    trailer_cost = 120000
    years = 20
    months = years * 12
    house_monthly_payment = house_cost / months
    trailer_monthly_payment = trailer_cost / months
    monthly_difference = house_monthly_payment - trailer_monthly_payment
    result = monthly_difference
    return result

print(solution())