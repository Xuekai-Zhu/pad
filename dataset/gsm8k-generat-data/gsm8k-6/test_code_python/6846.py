def solution():
    # Calculate how much money Isabella has
    giselle_money = 120
    isabella_money = giselle_money + 15
    sam_money = isabella_money - 45

    # Calculate the total money to be shared among the three shoppers
    total_money = giselle_money + isabella_money + sam_money

    # Calculate the amount each shopper will receive if they share the money equally
    amount_per_shopper = total_money / 3
    result = amount_per_shopper
    return result

print(solution())