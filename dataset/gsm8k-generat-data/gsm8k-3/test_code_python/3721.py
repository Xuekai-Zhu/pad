def solution():
    """Jessica is having a sweet tooth and bought 10 chocolate bars, 10 packs of gummy bears, and 20 bags of chocolate chips. Her total rang up to $150. If the cost of a pack of gummy bears is $2 and a bag of chocolate chips costs $5, how much does 1 chocolate bar cost?"""
    # Define the cost of each type of candy
    GUMMY_BEAR_PRICE = 2
    CHOCOLATE_CHIP_PRICE = 5

    # Define the number of each type of candy purchased
    chocolate_bars = 10
    gummy_bear_packs = 10
    chocolate_chip_bags = 20

    # Calculate the total cost of the gummy bears
    gummy_bear_cost = gummy_bear_packs * GUMMY_BEAR_PRICE

    # Calculate the total cost of the chocolate chips
    chocolate_chip_cost = chocolate_chip_bags * CHOCOLATE_CHIP_PRICE

    # Calculate the subtotal
    subtotal = 150 - gummy_bear_cost - chocolate_chip_cost

    # Calculate the cost per chocolate bar
    chocolate_bar_cost = subtotal / chocolate_bars

    # Display the cost per chocolate bar
    result = chocolate_bar_cost
    return result

print(solution())