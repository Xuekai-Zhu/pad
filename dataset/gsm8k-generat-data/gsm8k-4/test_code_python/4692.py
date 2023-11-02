def solution():
    """Bob and Johnny have a leaf raking business. They charge $4 for each bag of leaves they rake. On Monday they raked 5 bags of leaves. On Tuesday they raked 3 bags of leaves. On Wednesday, they counted their money and found they had $68 for all three days. How many bags of leaves did they rake on Wednesday?"""
    # Define the price per bag of leaves
    PRICE_PER_BAG = 4

    # Calculate the total earnings for Monday and Tuesday
    earnings_monday = 5 * PRICE_PER_BAG
    earnings_tuesday = 3 * PRICE_PER_BAG

    # Calculate the total earnings for all three days
    total_earnings = 68

    # Calculate the earnings from Wednesday
    earnings_wednesday = total_earnings - earnings_monday - earnings_tuesday

    # Calculate the number of bags of leaves raked on Wednesday
    bags_raked_wednesday = earnings_wednesday / PRICE_PER_BAG

    # return the result
    result = bags_raked_wednesday
    return result

print(solution())