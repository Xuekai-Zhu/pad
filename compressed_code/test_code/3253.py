def solution():
    
    old_tax_rate = 0.2
    new_tax_rate = 0.3
    old_income = 1000000
    new_income = 1500000
    old_taxes = old_income * old_tax_rate
    new_taxes = new_income * new_tax_rate
    tax_difference = new_taxes - old_taxes
    result = tax_difference
    return result

print(solution())