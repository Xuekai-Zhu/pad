def solution():
    """A country used to have a tax rate of 20%. They raised it to 30%. In that same time frame, John went from making 1,000,000 a year to 1,500,000 a year. How much more does he pay in taxes now compared to then?"""
    old_salary = 1000000
    new_salary = 1500000
    old_tax = old_salary * 0.2
    new_tax = new_salary * 0.3
    tax_increase = new_tax - old_tax
    result = tax_increase
    return result

print(solution())