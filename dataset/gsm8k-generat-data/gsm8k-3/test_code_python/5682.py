def solution():
    """Enrique earns a 15% commission on every piece of clothing item he sells.  In one day he sells 2 $700.00 suits, 6 shirts that cost $50.00 each and 2 pairs of loafers that cost $150.00 each.  How much commission does Enrique earn?"""
    # Define the commission rate
    COMMISSION_RATE = 0.15

    # Calculate the total sale amount for each type of clothing item
    suit_sale = 2 * 700
    shirt_sale = 6 * 50
    loafer_sale = 2 * 150

    # Calculate the total sale amount for all clothing items
    total_sale = suit_sale + shirt_sale + loafer_sale

    # Calculate the commission earned by Enrique
    commission = COMMISSION_RATE * total_sale

    # Display the commission earned by Enrique
    result = commission
    return result

print(solution())