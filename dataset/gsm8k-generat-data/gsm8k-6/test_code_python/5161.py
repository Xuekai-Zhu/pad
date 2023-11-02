def solution():
    # Calculate the value of the silver coins in copper coins
    silver_value = 8  # each silver coin is worth 8 copper coins
    total_silver_value = silver_value * 60

    # Calculate the value of the gold coins in copper coins
    gold_value = 3 * silver_value  # each gold coin is worth 3 silver coins
    total_gold_value = gold_value * 100

    # Calculate the total value of Smaug's hoard in copper coins
    total_value = total_silver_value + total_gold_value + 33  # adding the value of copper coins
    result = total_value
    return result

print(solution())