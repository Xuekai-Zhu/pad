def solution():
    """The cost of purchasing two commodities is $827. If the purchase price of the first one exceeds the other by $127, what is the purchase price of the first commodity?"""
    # Let x be the purchase price of the second commodity
    # Then the purchase price of the first commodity is x + 127
    # We know that the sum of the purchase prices is $827, so we have:
    # x + (x+127) = 827
    # Simplifying this equation, we get:
    # 2x + 127 = 827
    # 2x = 700
    # x = 350
    # Therefore, the purchase price of the first commodity is x + 127 = $477

    # Display the purchase price of the first commodity
    result = 477
    return result

print(solution())