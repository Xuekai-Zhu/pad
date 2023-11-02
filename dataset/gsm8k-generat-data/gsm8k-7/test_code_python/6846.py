def solution():
    giselle_money = 120

    # Calculate how much Isabella has
    isabella_money = giselle_money + 15

    # Calculate how much Sam has
    sam_money = isabella_money - 45

    # Calculate the total amount of money that will be shared equally
    total_money = giselle_money + isabella_money + sam_money

    # Calculate how much each shopper will receive
    amount_per_shopper = total_money / 3
    result = amount_per_shopper
    return result

print(solution())