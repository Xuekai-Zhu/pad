def solution():
    """Bob ordered 80 packs of Greek yogurt from Costco to use for the month. However, when the delivery arrived, he realized 40% of the packs were expired. He decided to return those packs. If each pack was $12, how much was Bob refunded for the expired product?"""
    total_packs = 80
    expired_packs = total_packs * 0.4
    non_expired_packs = total_packs - expired_packs
    pack_price = 12
    refund_amount = expired_packs * pack_price
    result = refund_amount
    return result

print(solution())