def solution():
    """Jenson and Kingsley have a tailoring business. Jenson makes 3 shirts, and Kingsley makes 5 pairs of pants per day. If each shirt uses 2 yards of fabric and a pair of pants uses 5 yards of fabric, how many yards of fabric do they need every 3 days?"""
    shirts_per_day = 3
    pants_per_day = 5
    days = 3
    yards_per_shirt = 2
    yards_per_pant = 5
    total_shirts = shirts_per_day * days
    total_pants = pants_per_day * days
    total_yards = (total_shirts * yards_per_shirt) + (total_pants * yards_per_pant)
    result = total_yards
    return result

print(solution())