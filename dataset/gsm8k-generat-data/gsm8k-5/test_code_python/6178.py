def solution():
    mp3_player_price = 120  # MP3 player costs 120 euros
    cd_price = 19  # CD costs 19 euros
    savings = 55  # Ibrahim has 55 euros in savings
    father_contribution = 20  # Ibrahim's father contributes 20 euros

    # Calculate the total cost of the purchase
    total_cost = mp3_player_price + cd_price

    # Calculate the total amount of money Ibrahim has
    total_money = savings + father_contribution

    # Calculate the amount of money Ibrahim lacks
    money_lack = total_cost - total_money
    result = money_lack
    return result

print(solution())