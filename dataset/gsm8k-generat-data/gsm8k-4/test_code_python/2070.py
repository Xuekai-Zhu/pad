def solution():
    """Bob ordered 80 packs of Greek yogurt from Costco to use for the month. However, when the delivery arrived, he realized 40% of the packs were expired. He decided to return those packs. If each pack was $12, how much was Bob refunded for the expired product?"""
    # Define the number of packs of Greek yogurt ordered and the percentage that was expired
    total_packs = 80
    expired_percentage = 0.4

    # Calculate the number of expired packs and the number of non-expired packs
    expired_packs = total_packs * expired_percentage
    non_expired_packs = total_packs - expired_packs

    # Calculate the refund amount for the expired packs
    refund_amount = expired_packs * 12

    # return the result
    result = round(refund_amount, 2)
    return result

print(solution())