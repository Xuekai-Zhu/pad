def solution():
    """Jerry takes 2 antacids that weigh 2 grams each and are 5% zinc by weight. Then he takes three more smaller antacids that weigh 1 gram each and have 15% zinc. How many milligrams of zinc does he eat?"""
    zinc_per_big_antacid = 0.05 * 2 * 1000  # Convert from grams to milligrams
    zinc_per_small_antacid = 0.15 * 1 * 1000
    total_zinc = 2 * zinc_per_big_antacid + 3 * zinc_per_small_antacid
    result = total_zinc
    return result

print(solution())