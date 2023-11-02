def solution():
    """Jacque arrived in France and his suitcase weighed 5 pounds.  While in France, he picked up 5 bottles of perfume that weighed 1.2 ounces each, 4 pounds of chocolate, 2 bars of soap that weighed 5 ounces each and 2 jars of jam that weighed 8 ounces each.  Considering 16 ounces is the same as 1 pound, how much did Jacque's suitcase weigh on the return flight home?"""
    # Define the weight conversions
    OUNCES_PER_POUND = 16

    # Define the initial weight of Jacque's suitcase
    suitcase_weight = 5

    # Calculate the weight of the perfume bottles
    perfume_weight = 5 * 1.2 / OUNCES_PER_POUND

    # Calculate the weight of the chocolate
    chocolate_weight = 4

    # Calculate the weight of the soap bars
    soap_weight = 2 * 5 / OUNCES_PER_POUND

    # Calculate the weight of the jam jars
    jam_weight = 2 * 8 / OUNCES_PER_POUND

    # Calculate the total weight of all items
    total_weight = suitcase_weight + perfume_weight + chocolate_weight + soap_weight + jam_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())