def solution():
    """John buys 20 bars of soap each weighing 1.5 pounds for $.5 per pound.  How much money did he spend on soap?"""
    # Define the weight of each soap bar and the price per pound
    SOAP_WEIGHT = 1.5
    PRICE_PER_POUND = 0.5

    # Calculate the total weight of the soap
    total_weight = 20 * SOAP_WEIGHT

    # Calculate the total cost of the soap
    total_cost = total_weight * PRICE_PER_POUND

    # Display the total cost
    result = total_cost
    return result

print(solution())