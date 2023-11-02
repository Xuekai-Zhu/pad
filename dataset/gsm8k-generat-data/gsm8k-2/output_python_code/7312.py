def solution():
    """James can make 4 hats out of one yard of velvet. He needs three yards of velvet to make a cloak. How much velvet does he need to make 6 cloaks and 12 hats?"""
    hats_per_yard = 4
    yards_per_cloak = 3
    cloaks = 6
    hats = 12
    total_hats = hats * cloaks
    total_hat_yards = total_hats / hats_per_yard
    total_cloak_yards = yards_per_cloak * cloaks
    total_yards = total_hat_yards + total_cloak_yards
    result = total_yards
    return result

print(solution())