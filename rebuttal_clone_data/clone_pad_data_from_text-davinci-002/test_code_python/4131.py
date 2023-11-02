def solution():
    take_home_salary = 40000
    property_taxes = 2000
    sales_taxes = 3000
    income_tax_rate = 10
    income_taxes = take_home_salary * (income_tax_rate / 100)
    total_taxes = property_taxes + sales_taxes + income_taxes
    gross_salary = take_home_salary + total_taxes
    result = gross_salary
    return result

print(solution())