def solution():
    """A pack of pretzels costs $4, while a pack of chips is 75% more expensive. Maciek went and bought two packets of chips and two packets of pretzels. How much did he pay for his purchases?"""
    # Define the cost of a pack of pretzels and the percentage increase for chips
    PRETZEL_PRICE = 4
    CHIPS_PERCENT_INCREASE = 75

    # Calculate the cost of a pack of chips
    chips_price = PRETZEL_PRICE + (PRETZEL_PRICE * CHIPS_PERCENT_INCREASE / 100)

    # Calculate the total cost of Maciek's purchases
    total_cost = 2 * PRETZEL_PRICE + 2 * chips_price

    # Display the total cost
    result = total_cost
    return result

print(solution())