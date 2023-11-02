def solution():
    """Isabella has $45 more than Sam but only $15 more than Giselle. If Giselle has $120, calculate the total amount of money each shopper will receive if Isabella, Sam, and Giselle donate the money to three shoppers at their local town's supermarket who then decides to share it equally."""
    giselle_money = 120
    isabella_money = giselle_money + 15
    sam_money = isabella_money - 45
    total_money = giselle_money + isabella_money + sam_money
    each_money = total_money / 3
    result = each_money
    return result

print(solution())