def solution():
    """Bennet is a farmer. He sells 20 of his eggplants for $3 each. He has 25 ears of corn that he can sell as well. If Bennet wants to make a total of $135, how much should he sell each ear of corn for?"""

    eggplant_price = 3
    eggplant_quantity = 20
    eggplant_total = eggplant_quantity * eggplant_price
    corn_total = 135 - eggplant_total
    corn_quantity = 25
    corn_price = corn_total / corn_quantity
    result = round(corn_price, 2)

    return result

print(solution())