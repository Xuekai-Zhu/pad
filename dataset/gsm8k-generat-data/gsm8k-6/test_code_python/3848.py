def solution():
    # Calculate the value of the coins after the increase
    increased_value = 15 * (5/3) # 2/3 increase equals 5/3 ratio
    # Calculate the total value of the 20 coins
    total_value = 20 * increased_value
    # Calculate the number of coins James needs to sell to recoup his original investment
    num_coins_to_sell = 20 * 15 / increased_value
    result = num_coins_to_sell
    return result

print(solution())