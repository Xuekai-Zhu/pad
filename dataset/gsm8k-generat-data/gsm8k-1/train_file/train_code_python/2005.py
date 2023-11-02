def solution():
    """Aaron pays his actuary membership fees each year. The membership fee increases yearly by $10. If he pays $80 in the first year, how much does his membership cost, in dollars, in the sixth year?"""
    initial_fee = 80
    yearly_increase = 10
    years_passed = 5 # we're calculating the fee for the 6th year, so 5 years have passed
    current_fee = initial_fee + (yearly_increase * years_passed)
    result = current_fee
    
    return result

print(solution())