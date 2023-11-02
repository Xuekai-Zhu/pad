def solution():
    """James buys steaks for buy one get one free. The price is $15 per pound and he buys 20 pounds. How much did he pay for the steaks?"""
    # Define the price per pound and the number of pounds purchased
    PRICE_PER_POUND = 15
    POUNDS_PURCHASED = 20

    # Calculate the total price without the buy one get one free offer
    total_price = PRICE_PER_POUND * POUNDS_PURCHASED

    # Calculate the price with the offer
    price_with_offer = total_price / 2

    # Return the result
    result = price_with_offer
    return result

print(solution())