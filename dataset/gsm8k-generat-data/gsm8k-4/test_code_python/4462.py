def solution():
    """John buys 20 bars of soap each weighing 1.5 pounds for $.5 per pound. How much money did he spend on soap?"""
    # Define the weight and price of each bar of soap
    soap_weight = 1.5  # pounds
    soap_price_per_pound = 0.5  # dollars

    # Calculate the total weight of soap purchased
    total_weight = 20 * soap_weight

    # Calculate the total cost of soap purchased
    total_cost = total_weight * soap_price_per_pound

    # return the result
    result = total_cost
    return result

print(solution())