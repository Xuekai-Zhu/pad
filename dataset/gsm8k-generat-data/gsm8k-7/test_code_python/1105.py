def solution():
    initial_money = 400
    mom_money = initial_money / 4
    clothes_money = initial_money / 8
    charity_money = initial_money / 5

    # Calculate the total amount of money given away
    money_given_away = mom_money + clothes_money + charity_money

    # Calculate the amount of money remaining
    remaining_money = initial_money - money_given_away
    result = remaining_money
    return result

print(solution())