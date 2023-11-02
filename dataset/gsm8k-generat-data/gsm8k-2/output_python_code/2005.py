def solution():
    """Aaron pays his actuary membership fees each year. The membership fee increases yearly by $10. If he pays $80 in the first year, how much does his membership cost, in dollars, in the sixth year?"""
    first_year_fee = 80
    annual_increase = 10
    sixth_year_fee = first_year_fee + 5 * annual_increase
    result = sixth_year_fee
    return result

print(solution())