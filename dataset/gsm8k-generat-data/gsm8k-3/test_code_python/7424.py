def solution():
    """In the honey shop, the bulk price of honey is $5 per pound and the minimum spend is $40 before tax. The honey is taxed at $1 per pound. If Penny has paid $240 for honey, by how many pounds has Penny’s purchase exceed the minimum spend?"""
    # Define the bulk price and tax rate for honey
    BULK_PRICE = 5
    TAX_RATE = 1

    # Define the minimum spend before tax
    MINIMUM_SPEND = 40

    # Calculate the amount of honey Penny purchased before tax
    honey_purchased = (240 - MINIMUM_SPEND) / (BULK_PRICE + TAX_RATE)

    # Calculate the amount of honey Penny purchased above the minimum spend
    honey_above_minimum = honey_purchased - 8

    # Display the amount of honey purchased above the minimum spend
    result = honey_above_minimum
    return result

print(solution())