def solution():
    """Leila spent $40 which is 1/4 of her money on a sweater. She was then left with $20 after spending the rest of her money on buying pieces of jewelry. How much more did Leila spend on jewelry than on the sweater?"""
    total_money = 4 * 40 # since 40 is 1/4 of her money
    sweater_cost = 40
    jewelry_cost = total_money - sweater_cost - 20 # remaining money after buying sweater and having $20 left
    difference = jewelry_cost - sweater_cost
    result = difference
    return result

print(solution())