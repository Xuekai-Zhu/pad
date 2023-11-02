def solution():
    """Carl has been selling watermelons on the side of the road for $3 each. This evening he went home with $105 in profit and 18 watermelons. How many watermelons did he start out with this morning?"""
    # Define the selling price per watermelon and the profit
    SELLING_PRICE = 3
    PROFIT = 105

    # Calculate the cost of the watermelons
    cost = PROFIT + (SELLING_PRICE * 18)

    # Calculate the number of watermelons Carl started with
    starting_watermelons = cost // SELLING_PRICE

    # Display the number of watermelons Carl started with
    result = starting_watermelons
    return result

print(solution())