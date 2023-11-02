def solution():
    """Will's mom gave him $74 to go shopping. He bought a sweater for $9, a T-shirt for $11 and a pair of shoes for $30. He then returned his shoes for a 90% refund. How much money does Will have left?"""
    initial_money = 74
    sweater_cost = 9
    tshirt_cost = 11
    shoes_cost = 30
    shoes_refund = shoes_cost * 0.9
    total_cost = sweater_cost + tshirt_cost + (shoes_cost - shoes_refund)
    left_money = initial_money - total_cost
    result = left_money
    return result

print(solution())