def solution():
    """Jenson and Kingsley have a tailoring business. Jenson makes 3 shirts, and Kingsley makes 5 pairs of pants per day. If each shirt uses 2 yards of fabric and a pair of pants uses 5 yards of fabric, how many yards of fabric do they need every 3 days?"""
    jenson_shirts_per_day = 3
    kingsley_pants_per_day = 5
    fabric_per_shirt = 2
    fabric_per_pants = 5
    total_days = 3
    total_jenson_shirts = jenson_shirts_per_day * total_days
    total_kingsley_pants = kingsley_pants_per_day * total_days
    total_fabric = (total_jenson_shirts * fabric_per_shirt) + (total_kingsley_pants * fabric_per_pants)
    result = total_fabric
    return result

print(solution())