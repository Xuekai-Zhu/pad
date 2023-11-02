def solution():
    
    total_earnings = 8000
    zachary_babysit = 600
    julie_babysit = 3 * zachary_babysit
    chloe_babysit = 5 * zachary_babysit
    total_babysit_earnings = zachary_babysit + julie_babysit + chloe_babysit
    pool_cleaning_earnings = total_earnings - total_babysit_earnings
    result = pool_cleaning_earnings
    return result

print(solution())