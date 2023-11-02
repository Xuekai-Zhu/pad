def solution():
    """Jackson wants to impress his girlfriend by filling her hot tub with champagne. The hot tub holds 40 gallons of liquid. Each bottle of champagne holds 1 quart. (There are 4 quarts per gallon). If each bottle of champagne costs $50, but Jackson gets a 20% volume discount, how much does he spend on champagne?"""
    # Define the number of quarts needed to fill the hot tub
    quarts_needed = 40 * 4

    # Define the number of bottles needed to fill the hot tub
    bottles_needed = quarts_needed / 4

    # Calculate the cost of the bottles before the discount
    total_cost_before_discount = bottles_needed * 50

    # Calculate the discount
    discount = 0.2 * total_cost_before_discount

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost_before_discount - discount

    # Display the total cost
    result = total_cost_after_discount
    return result

print(solution())