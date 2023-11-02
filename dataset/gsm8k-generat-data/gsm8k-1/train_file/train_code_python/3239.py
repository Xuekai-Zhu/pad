def solution():
    """Leila spent $40 which is 1/4 of her money on a sweater. She was then left with $20 after spending the rest of her money on buying pieces of jewelry. How much more did Leila spend on jewelry than on the sweater?"""
    total_money = 40 * 4
    money_spent_on_jewelry = total_money - 40 - 20
    money_spent_on_sweater = 40
    difference = money_spent_on_jewelry - money_spent_on_sweater
    result = difference
    
    return result

print(solution())