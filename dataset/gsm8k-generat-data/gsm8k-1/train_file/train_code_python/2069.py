def solution():
    """Bob ordered 80 packs of Greek yogurt from Costco to use for the month. However, when the delivery arrived, he realized 40% of the packs were expired. He decided to return those packs. If each pack was $12, how much was Bob refunded for the expired product?"""
    total_packs = 80
    expired_packs = total_packs * 0.4
    refunded_packs = expired_packs * 12
    result = refunded_packs
    return result

print(solution())