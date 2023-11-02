def solution():
    """Andy bakes and sells birthday cakes. To make two cakes he spends $12 on ingredients, and $1 on packaging for each cake. Andy sells each cake for $15. How much money does Andy make for each cake?"""
    # Define the cost of ingredients and packaging per cake
    INGREDIENTS_COST = 12 / 2
    PACKAGING_COST = 1

    # Define the selling price per cake
    SELLING_PRICE = 15

    # Calculate the profit per cake
    profit_per_cake = SELLING_PRICE - INGREDIENTS_COST - PACKAGING_COST

    # Display the profit per cake
    result = profit_per_cake
    return result

print(solution())