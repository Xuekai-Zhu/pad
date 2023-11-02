def solution():
    """A watermelon weighs 23 pounds. If Farmer Kent sells his special watermelons for $2 a pound, how much money would he make for selling 18 watermelons of the same weight?"""
    # Define the weight and selling price of each watermelon
    WATERMELON_WEIGHT = 23
    SELLING_PRICE = 2

    # Calculate the total weight and selling price for 18 watermelons
    total_weight = WATERMELON_WEIGHT * 18
    total_price = total_weight * SELLING_PRICE

    # return the result
    result = total_price
    return result

print(solution())