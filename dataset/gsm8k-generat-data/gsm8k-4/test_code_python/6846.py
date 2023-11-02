def solution():
    """Isabella has $45 more than Sam but only $15 more than Giselle. If Giselle has $120, calculate the total amount of money each shopper will receive if Isabella, Sam, and Giselle donate the money to three shoppers at their local town's supermarket who then decides to share it equally."""
    # Define Giselle's amount of money
    giselle_money = 120

    # Calculate Isabella's amount of money
    isabella_money = giselle_money + 15

    # Calculate Sam's amount of money
    sam_money = isabella_money - 45

    # Calculate the total amount of money
    total_money = giselle_money + isabella_money + sam_money

    # Calculate the amount of money each shopper will receive
    each_shopper_money = total_money / 3

    result = each_shopper_money
    return result

print(solution())