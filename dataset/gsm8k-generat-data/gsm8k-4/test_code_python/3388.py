def solution():
    """Jacque arrived in France and his suitcase weighed 5 pounds. While in France, he picked up 5 bottles of perfume that weighed 1.2 ounces each, 4 pounds of chocolate, 2 bars of soap that weighed 5 ounces each and 2 jars of jam that weighed 8 ounces each. Considering 16 ounces is the same as 1 pound, how much did Jacque's suitcase weigh on the return flight home?"""
    # Define the initial weight of the suitcase
    suitcase_weight = 5

    # Calculate the weight of the perfume bottles in pounds
    perfume_weight = 5 * 1.2 / 16

    # Calculate the weight of the chocolate in pounds
    chocolate_weight = 4

    # Calculate the weight of the soap bars in pounds
    soap_weight = 2 * 5 / 16

    # Calculate the weight of the jam jars in pounds
    jam_weight = 2 * 8 / 16

    # Calculate the final weight of the suitcase
    final_weight = suitcase_weight + perfume_weight + chocolate_weight + soap_weight + jam_weight

    # return the result
    result = round(final_weight, 2)
    return result

print(solution())