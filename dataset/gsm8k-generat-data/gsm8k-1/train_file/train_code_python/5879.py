def solution():
    """Nedy can eat 8 packs of crackers from Monday to Thursday. If Nedy ate twice the amount on Friday, how many crackers did Nedy eat in all?"""
    packs_per_day = 8
    days_except_friday = 4
    packs_on_friday = packs_per_day * 2
    total_packs = packs_per_day * days_except_friday + packs_on_friday
    result = total_packs
    return result

print(solution())