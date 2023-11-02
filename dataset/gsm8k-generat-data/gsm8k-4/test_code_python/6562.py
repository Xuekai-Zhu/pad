def solution():
    """A pack of pretzels costs $4, while a pack of chips is 75% more expensive. Maciek went and bought two packets of chips and two packets of pretzels. How much did he pay for his purchases?"""
    # Define the price of pretzels and the percentage increase of chips
    pretzel_price = 4
    chips_increase = 0.75

    # Calculate the price of chips
    chips_price = pretzel_price * (1 + chips_increase)

    # Calculate the total cost of Maciek's purchases
    total_cost = 2 * pretzel_price + 2 * chips_price

    # return the result
    result = total_cost
    return result

print(solution())