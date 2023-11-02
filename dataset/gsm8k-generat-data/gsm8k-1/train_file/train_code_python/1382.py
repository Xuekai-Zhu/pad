def solution():
    """Issac has to buy pens and pencils for the upcoming school year. Issac buys 108 writing utensils total. He buys 12 more than 5 times the number of pencils than pens. How many pens did Issac buy?"""
    total_utensils = 108
    pencils = (total_utensils - 12) / 6
    pens = total_utensils - pencils
    result = pens
    return result

print(solution())