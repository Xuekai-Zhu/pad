def solution():
    """If Isabella has $45 more than Sam but only $15 more than Giselle, and Giselle has $120, calculate the total amount of money each shopper will receive if Isabella, Sam, and Giselle donate the money to three shoppers at their local town's supermarket who then decide to share it equally."""
    giselle_money = 120
    isabella_money = giselle_money + 15
    sam_money = isabella_money - 45

    total_money = isabella_money + sam_money + giselle_money
    equally_shared_money = total_money / 3

    result = equally_shared_money
    return result

print(solution())