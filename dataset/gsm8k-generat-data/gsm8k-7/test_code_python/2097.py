def solution():
    total_money = 67

    # Let x be the amount of money Nada has
    # Then Ali has x - 5
    # And John has 4x

    x = (total_money + 5) / 6
    john_money = 4 * x
    result = john_money
    return result

print(solution())