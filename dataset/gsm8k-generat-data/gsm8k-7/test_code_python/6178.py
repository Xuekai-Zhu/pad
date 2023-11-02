def solution():
    mp3_player_price = 120
    cd_price = 19
    savings = 55
    father_contribution = 20

    # Calculate the total price of all items
    total_price = mp3_player_price + cd_price

    # Calculate the total amount of money Ibrahim has
    total_money = savings + father_contribution

    # Calculate the amount of money that Ibrahim lacks
    money_lack = total_price - total_money
    result = money_lack
    return result

print(solution())