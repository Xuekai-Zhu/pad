def solution():
    """Will's mom gave him $74 to go shopping. He bought a sweater for $9, a T-shirt for $11 and a pair of shoes for $30. He then returned his shoes for a 90% refund. How much money does Will have left?"""
    total_spent = 9 + 11 + 30
    shoes_refund = 0.9 * 30
    total_spent -= shoes_refund
    money_left = 74 - total_spent
    result = money_left
    return result

print(solution())