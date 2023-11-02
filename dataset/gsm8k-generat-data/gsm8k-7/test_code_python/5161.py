def solution():
    num_gold_coins = 100
    num_silver_coins = 60
    num_copper_coins = 33

    value_of_silver_coin = 8   # in terms of copper coins
    value_of_gold_coin = value_of_silver_coin * 3   # in terms of copper coins

    # Calculate the total value of all gold coins in terms of copper coins
    total_gold_value = num_gold_coins * value_of_gold_coin

    # Calculate the total value of all silver coins in terms of copper coins
    total_silver_value = num_silver_coins * value_of_silver_coin

    # Calculate the total value of all copper coins
    total_copper_value = num_copper_coins

    # Calculate the total value of Smaug's hoard in terms of copper coins
    total_value = total_gold_value + total_silver_value + total_copper_value
    result = total_value
    return result

print(solution())