def solution():
    """Bob ordered 80 packs of Greek yogurt from Costco to use for the month. However, when the delivery arrived, he realized 40% of the packs were expired. He decided to return those packs. If each pack was $12, how much was Bob refunded for the expired product?"""
    # Define the total number of packs ordered
    total_packs = 80

    # Calculate the number of expired packs
    expired_packs = total_packs * 0.4

    # Calculate the refund amount
    refund = expired_packs * 12

    # Display the refund amount
    result = refund
    return result

print(solution())