def solution():
    """Annalise was sent by her mother to the store to buy 10 boxes of Kleenex Ultra Soft Facial Tissues. If each box has 20 packs of tissues and each pack contain 100 tissues sold at five cents each, calculate the total amount of money Annalise spent to buy the ten boxes."""
    # Define the price of one tissue pack
    TISSUE_PRICE = 0.05

    # Calculate the total number of packs of tissues
    packs = 10 * 20

    # Calculate the total number of tissues
    tissues = packs * 100

    # Calculate the total cost of the tissues
    cost = tissues * TISSUE_PRICE

    # Display the total cost
    result = cost
    return result

print(solution())