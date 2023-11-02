def solution():
    
    take_home_salary = 40000
    property_taxes = 2000
    sales_taxes = 3000
    net_income = take_home_salary + property_taxes + sales_taxes
    income_tax_rate = 0.1
    gross_income = net_income / (1 - income_tax_rate)
    result = gross_income
    return result

print(solution())