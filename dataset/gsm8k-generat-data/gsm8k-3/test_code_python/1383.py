def solution():
    """Issac has to buy pens and pencils for the upcoming school year. Issac buys 108 writing utensils total. He buys 12 more than 5 times the number of pencils than pens. How many pens did Issac buy?"""
    # Let's assume that x is the number of pens and y is the number of pencils bought by Issac
    # We know that:
    # x + y = 108 (total number of writing utensils bought)
    # y = 5x + 12 (number of pencils bought is 12 more than 5 times the number of pens)

    # Substituting the second equation into the first equation:
    x + (5x + 12) = 108
    # Simplifying:
    6x + 12 = 108
    6x = 96
    x = 16

    # Issac bought 16 pens
    result = 16
    return result

print(solution())