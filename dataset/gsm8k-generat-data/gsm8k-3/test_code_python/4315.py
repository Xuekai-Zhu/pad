def solution():
    """A watermelon weighs 23 pounds. If Farmer Kent sells his special watermelons for $2 a pound, how much money would he make for selling 18 watermelons of the same weight?"""
    # Define the weight of each watermelon and the selling price per pound
    WEIGHT = 23
    PRICE_PER_POUND = 2

    # Calculate the total weight of all the watermelons
    total_weight = 18 * WEIGHT

    # Calculate the total selling price of all the watermelons
    total_price = total_weight * PRICE_PER_POUND

    # Display the total selling price
    result = total_price
    return result

print(solution())