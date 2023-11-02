def solution():
    """A chocolate bar weighs 125 g. A shopkeeper has just received a 2 kilogram box of chocolate. How many bars does this represent?"""
    # Define the weight of a chocolate bar in grams
    BAR_WEIGHT = 125

    # Define the weight of the chocolate box
    BOX_WEIGHT = 2000

    # Calculate the number of chocolate bars in the box
    num_bars = BOX_WEIGHT // BAR_WEIGHT

    # Return the result
    result = num_bars
    return result

print(solution())