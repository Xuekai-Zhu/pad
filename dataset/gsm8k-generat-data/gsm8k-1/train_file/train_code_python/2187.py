def solution():
    """Jerry takes 2 antacids that weigh 2 grams each and are 5% zinc by weight. Then he takes three more smaller antacids that weigh 1 gram each and have 15% zinc. How many milligrams of zinc does he eat?"""
    big_antacid_weight = 2
    small_antacid_weight = 1
    big_antacid_zinc_percent = 5
    small_antacid_zinc_percent = 15
    
    total_weight = 2 * big_antacid_weight + 3 * small_antacid_weight
    total_zinc_weight = (2 * big_antacid_weight * big_antacid_zinc_percent / 100) + (3 * small_antacid_weight * small_antacid_zinc_percent / 100)
    zinc_in_milligrams = total_zinc_weight * 1000
    
    result = zinc_in_milligrams
    return result

print(solution())