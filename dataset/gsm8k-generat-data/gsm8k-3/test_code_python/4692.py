def solution():
    """Bob and Johnny have a leaf raking business. They charge $4 for each bag of leaves they rake. On Monday they raked 5 bags of leaves. On Tuesday they raked 3 bags of leaves. On Wednesday, they counted their money and found they had $68 for all three days. How many bags of leaves did they rake on Wednesday?"""
    # Define the price per bag of leaves and the total amount earned
    PRICE_PER_BAG = 4
    TOTAL_EARNED = 68

    # Calculate the total number of bags raked on Monday and Tuesday
    total_bags = 5 + 3

    # Calculate the number of bags raked on Wednesday
    bags_on_wednesday = (TOTAL_EARNED - (total_bags * PRICE_PER_BAG)) / PRICE_PER_BAG

    # Display the number of bags raked on Wednesday
    result = bags_on_wednesday
    return result

print(solution())