def solution():
    """Zoe made a total of $8,000 cleaning pools and babysitting. She babysat Julie three times as often as she babysat Zachary. The number of times she babysat Zachary was 1/5 the number of times she babysat Chloe. If Zoe made $600 babysitting Zachary, how much did she earn from pool cleaning?"""
    total_earnings = 8000
    earnings_from_zachary = 600
    julie_to_zachary_ratio = 3
    chloe_to_zachary_ratio = 5
    total_babysitting_ratio = 1 + julie_to_zachary_ratio + chloe_to_zachary_ratio
    earnings_from_babysitting = total_earnings - earnings_from_zachary
    zoe_share_of_babysitting = earnings_from_babysitting / total_babysitting_ratio
    earnings_from_pool_cleaning = total_earnings - earnings_from_zachary - zoe_share_of_babysitting
    result = earnings_from_pool_cleaning
    return result

print(solution())