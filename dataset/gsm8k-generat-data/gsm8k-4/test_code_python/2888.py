def solution():
    """A liter of chlorine costs $10 and is now sold at 20% off. A box of soap that costs $16 is now sold at 25% off. How much will you save if you buy 3 liters of chlorine and 5 boxes of soap?"""
    # Define the prices and discounts
    chlorine_price = 10
    chlorine_discount = 0.2
    soap_price = 16
    soap_discount = 0.25

    # Calculate the total cost of the chlorine and soap before discounts
    total_chlorine_cost = chlorine_price * 3
    total_soap_cost = soap_price * 5

    # Calculate the discounted price of the chlorine and soap
    discounted_chlorine_price = chlorine_price * (1 - chlorine_discount)
    discounted_soap_price = soap_price * (1 - soap_discount)

    # Calculate the total cost of the chlorine and soap after discounts
    total_discounted_chlorine_cost = discounted_chlorine_price * 3
    total_discounted_soap_cost = discounted_soap_price * 5

    # Calculate the total savings
    total_savings = (total_chlorine_cost - total_discounted_chlorine_cost) + (total_soap_cost - total_discounted_soap_cost)

    result = total_savings
    return result

print(solution())