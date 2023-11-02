def solution():
    # Calculate the value of the silver coins in terms of copper coins
    silver_value = 8

    # Calculate the value of the gold coins in terms of copper coins
    gold_value = 3 * silver_value

    # Calculate the total value of Smaug's hoard in terms of copper coins
    total_value = 100 * gold_value + 60 * silver_value + 33

    result = total_value
    return result

print(solution())