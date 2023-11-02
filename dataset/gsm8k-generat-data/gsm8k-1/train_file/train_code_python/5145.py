def solution():
    """The bagels cost $2.25 each, or a dozen for $24. How much is saved, per bagel, in cents, by buying a dozen at a time?"""
    individual_price = 2.25
    dozen_price = 24
    bagels_per_dozen = 12
    price_per_bagel = individual_price / bagels_per_dozen
    savings = individual_price - price_per_bagel
    savings_in_cents = savings * 100
    
    return savings_in_cents

print(solution())