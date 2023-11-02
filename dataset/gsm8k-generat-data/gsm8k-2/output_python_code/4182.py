def solution():
    """A country used to have a tax rate of 20%. They raised it to 30%. In that same time frame, John went from making 1,000,000 a year to 1,500,000 a year. How much more does he pay in taxes now compared to then?"""
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