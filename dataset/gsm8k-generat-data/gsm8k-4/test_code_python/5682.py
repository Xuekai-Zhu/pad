def solution():
    """Enrique earns a 15% commission on every piece of clothing item he sells. In one day he sells 2 $700.00 suits, 6 shirts that cost $50.00 each and 2 pairs of loafers that are $150.00 each. How much commission does Enrique earn?"""
    # Calculate the commission from selling the suits
    suit_commission = 2 * 700 * 0.15

    # Calculate the commission from selling the shirts
    shirt_commission = 6 * 50 * 0.15

    # Calculate the commission from selling the loafers
    loafer_commission = 2 * 150 * 0.15

    # Calculate the total commission
    total_commission = suit_commission + shirt_commission + loafer_commission

    result = total_commission
    return result

print(solution())