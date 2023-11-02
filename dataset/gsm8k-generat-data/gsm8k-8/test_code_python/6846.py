def solution():
    # Calculate the amount of money Isabella has
    giselle_money = 120
    isabella_money = giselle_money + 15
    sam_money = isabella_money - 45

    # Calculate the total amount of money to be shared
    total_money = giselle_money + isabella_money + sam_money

    # Calculate the amount each shopper will receive
    each_shopper = total_money / 3
    result = each_shopper
    return result

print(solution())