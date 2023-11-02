def solution():
    # Calculate the original cost of 3 liters of chlorine and 5 boxes of soap
    orig_chlorine_cost = 3 * 10
    orig_soap_cost = 5 * 16

    # Calculate the discounted price after 20% off on chlorine and 25% off on soap
    disc_chlorine_price = orig_chlorine_cost * (1 - 0.2)
    disc_soap_price = orig_soap_cost * (1 - 0.25)

    # Calculate the amount saved by buying at discounted prices
    amt_saved = orig_chlorine_cost - disc_chlorine_price + orig_soap_cost - disc_soap_price
    result = amt_saved
    return result

print(solution())