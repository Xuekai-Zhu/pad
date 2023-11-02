def solution():
    """Carl has been selling watermelons on the side of the road for $3 each. This evening he went home with $105 in profit and 18 watermelons. How many watermelons did he start out with this morning?"""
    # Define the price and profit per watermelon
    PRICE_PER_WATERMELON = 3
    PROFIT_PER_WATERMELON = PRICE_PER_WATERMELON - 1.5

    # Calculate the total profit
    total_profit = 105

    # Calculate the number of watermelons sold
    watermelons_sold = total_profit / PROFIT_PER_WATERMELON

    # Calculate the number of watermelons started with
    watermelons_started = watermelons_sold + 18

    # return the result
    result = watermelons_started
    return result

print(solution())