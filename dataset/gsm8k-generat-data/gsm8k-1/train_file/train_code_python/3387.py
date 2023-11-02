def solution():
    """Jacque arrived in France and his suitcase weighed 5 pounds. While in France, he picked up 5 bottles of perfume that weighed 1.2 ounces each, 4 pounds of chocolate, 2 bars of soap that weighed 5 ounces each and 2 jars of jam that weighed 8 ounces each. Considering 16 ounces is the same as 1 pound, how much did Jacque's suitcase weigh on the return flight home?"""
    initial_weight = 5
    perfume_weight = 5 * 1.2 / 16  # convert ounces to pounds
    chocolate_weight = 4
    soap_weight = 2 * 5 / 16  # convert ounces to pounds
    jam_weight = 2 * 8 / 16  # convert ounces to pounds
    return_weight = initial_weight + perfume_weight + chocolate_weight + soap_weight + jam_weight
    result = return_weight
    return result

print(solution())