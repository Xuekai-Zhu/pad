def solution():
    """Smaug the dragon hoards 100 gold coins, 60 silver coins, and 33 copper coins. If each silver coin is worth 8 copper coins, and each gold coin is worth 3 silver coins, what is the total value of Smaug's hoard expressed as a number of copper coins?"""
    # Define the value of each type of coin in copper coins
    GOLD_VALUE = 3 * 8
    SILVER_VALUE = 8
    COPPER_VALUE = 1

    # Calculate the total value of the gold coins in copper coins
    gold_total = 100 * GOLD_VALUE

    # Calculate the total value of the silver coins in copper coins
    silver_total = 60 * SILVER_VALUE

    # Calculate the total value of the copper coins in copper coins
    copper_total = 33 * COPPER_VALUE

    # Calculate the total value of Smaug's hoard in copper coins
    hoard_total = gold_total + silver_total + copper_total

    # Display the total value in copper coins
    result = hoard_total
    return result

print(solution())