def solution():
    """Smaug the dragon hoards 100 gold coins, 60 silver coins, and 33 copper coins. If each silver coin is worth 8 copper coins, and each gold coin is worth 3 silver coins, what is the total value of Smaug's hoard expressed as a number of copper coins?"""
    # Define the values of each coin
    gold_value = 3 * 8
    silver_value = 8
    copper_value = 1

    # Calculate the total value of each type of coin in copper coins
    total_gold_value = gold_value * 100
    total_silver_value = silver_value * 60
    total_copper_value = copper_value * 33

    # Calculate the total value of Smaug's hoard in copper coins
    total_value = total_gold_value + total_silver_value + total_copper_value

    # return the result
    result = total_value
    return result

print(solution())