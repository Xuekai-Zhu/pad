def solution():
    coins_bought = 20  # James buys 20 coins
    cost_per_coin = 15  # James pays $15 per coin

    # Calculate the total cost of buying the coins
    total_cost = coins_bought * cost_per_coin

    # Calculate the new value of the coins after increasing by 2/3
    increased_value = (2/3 + 1) * cost_per_coin

    # Calculate the number of coins James needs to sell to recoup his original investment
    coins_to_sell = total_cost / increased_value
    result = coins_to_sell
    return result

print(solution())