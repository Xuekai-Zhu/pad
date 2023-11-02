def solution():
    """Zoe made a total of $8,000 cleaning pools and babysitting. She babysat Julie three times as often as she babysat Zachary. The number of times she babysat Zachary was 1/5 the number of times she babysat Chloe. If Zoe made $600 babysitting Zachary, how much did she earn from pool cleaning?"""
    total_earnings = 8000
    zachary_babysit = 600
    julie_babysit = 3 * zachary_babysit
    chloe_babysit = 5 * zachary_babysit
    total_babysit_earnings = zachary_babysit + julie_babysit + chloe_babysit
    pool_cleaning_earnings = total_earnings - total_babysit_earnings
    result = pool_cleaning_earnings
    return result

print(solution())