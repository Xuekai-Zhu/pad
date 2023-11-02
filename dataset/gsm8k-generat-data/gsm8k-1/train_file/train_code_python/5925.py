def solution():
    """Jack has 42 pounds, 11 euros, and 3000 yen. If there are 2 pounds per euro and 100 yen per pound, how much does Jack have in yen?"""
    pounds = 42
    euros = 11
    yen = 3000
    pounds_in_euros = pounds * 2
    total_euros = euros + (pounds_in_euros)
    total_pounds = pounds + pounds_in_euros
    total_yen = yen + (total_pounds * 100)
    result = total_yen
    
    return result

print(solution())