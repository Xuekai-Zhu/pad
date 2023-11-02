def solution():
    """James can make 4 hats out of one yard of velvet. He needs three yards of velvet to make a cloak. How much velvet does he need to make 6 cloaks and 12 hats?"""
    hats_per_yard = 4
    cloaks_per_yard = 1/3
    total_cloaks = 6
    total_hats = 12
    total_hats_yards = total_hats / hats_per_yard
    total_cloaks_yards = total_cloaks / cloaks_per_yard
    total_yards = total_hats_yards + total_cloaks_yards
    result = total_yards
    return result

print(solution())