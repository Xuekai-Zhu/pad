def solution():
    bagel_price = 2.25  # price of one bagel
    dozen_price = 24  # price of a dozen bagels
    bagels_per_dozen = 12  # number of bagels in a dozen

    # Calculate the price per bagel when buying a dozen
    price_per_dozen = dozen_price / bagels_per_dozen
    price_per_bagel = price_per_dozen / 100  # convert price to cents

    # Calculate the savings per bagel when buying a dozen
    savings_per_bagel = bagel_price - price_per_bagel
    savings_per_bagel_cents = savings_per_bagel * 100  # convert savings to cents
    result = savings_per_bagel_cents
    return result

print(solution())