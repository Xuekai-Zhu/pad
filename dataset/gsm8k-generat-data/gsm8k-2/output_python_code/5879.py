def solution():
    """Nedy can eat 8 packs of crackers from Monday to Thursday. If Nedy ate twice the amount on Friday, how many crackers did Nedy eat in all?"""
    total_packs = 0
    for day in range(1, 6):
        if day < 5:
            total_packs += 8
        else:
            total_packs += 16
    total_crackers = total_packs * 12
    result = total_crackers
    return result

print(solution())