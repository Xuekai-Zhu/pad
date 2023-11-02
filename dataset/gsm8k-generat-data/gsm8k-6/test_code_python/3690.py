def solution():
    # Find Sandy's current age
    Sandy_age = 10 * (Sandy_monthly_bill / 10)
    
    # Find the age difference between Sandy and Kim in 2 years
    age_difference = (Sandy_age + 2) - 3*(Kim_age + 2)
    
    # Find Sandy's monthly phone bill expense
    Sandy_monthly_bill = Sandy_age * 10
    
    result = Sandy_monthly_bill
    return result

print(solution())