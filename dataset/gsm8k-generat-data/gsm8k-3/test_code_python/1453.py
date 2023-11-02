def solution():
    """A chocolate bar weighs 125 g. A shopkeeper has just received a 2 kilogram box of chocolate. How many bars does this represent?"""
    # Define the weight of a single chocolate bar in grams
    BAR_WEIGHT = 125

    # Convert the weight of the box from kilograms to grams
    box_weight = 2000

    # Calculate the number of chocolate bars in the box
    num_bars = box_weight // BAR_WEIGHT

    # Display the number of chocolate bars
    result = num_bars
    return result

print(solution())