def solution():
    carmela_money = 7
    cousin_money = 2
    num_cousins = 4

    # Calculate total amount of money among Carmela and her cousins
    total_money = carmela_money + (num_cousins * cousin_money)

    # Calculate the amount of money each person should have after equal distribution
    equal_money = total_money / (num_cousins + 1)

    # Calculate the amount of money that Carmela needs to give to each of her cousins
    money_to_give = equal_money - cousin_money
    result = money_to_give
    return result

print(solution())