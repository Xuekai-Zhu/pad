def solution():
    """A liter of chlorine costs $10 and is now sold at 20% off. A box of soap that costs $16 is now sold at 25% off. How much will you save if you buy 3 liters of chlorine and 5 boxes of soap?"""
    # Define the original prices and discounts
    CHLORINE_PRICE = 10
    CHLORINE_DISCOUNT = 0.2
    SOAP_PRICE = 16
    SOAP_DISCOUNT = 0.25

    # Calculate the discounted prices
    chlorine_discounted_price = CHLORINE_PRICE - (CHLORINE_PRICE * CHLORINE_DISCOUNT)
    soap_discounted_price = SOAP_PRICE - (SOAP_PRICE * SOAP_DISCOUNT)

    # Calculate the total savings
    chlorine_savings = 3 * (CHLORINE_PRICE - chlorine_discounted_price)
    soap_savings = 5 * (SOAP_PRICE - soap_discounted_price)
    total_savings = chlorine_savings + soap_savings

    # Display the total savings
    result = total_savings
    return result

print(solution())