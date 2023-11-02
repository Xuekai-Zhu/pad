def solution():
    """Andy bakes and sells birthday cakes. To make two cakes he spends $12 on ingredients, and $1 on packaging for each cake. Andy sells each cake for $15. How much money does Andy make for each cake?"""
    # Define the cost of ingredients and packaging for two cakes
    TWO_CAKES_COST = 12 + 2*1 

    # Define the selling price of one cake
    CAKE_SELLING_PRICE = 15

    # Calculate the profit for one cake
    profit_per_cake = CAKE_SELLING_PRICE - (TWO_CAKES_COST / 2)

    # Return the profit
    result = profit_per_cake
    return result

print(solution())