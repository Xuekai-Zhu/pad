def solution():
    """Mark went to a store where he spent one-half of his money, and then spent $14 more. He then went to another store where he spent one-third of his starting money, and then spent $16 more. If he then had no money left, how much did he have when he entered the first store?"""
    x = 0
    while True:
        x += 1
        if (x / 2 - 14) / 3 - 16 == x / 6:
            result = x
            break
    return result

# Note: This problem does not have a unique solution, as there are multiple values of x that satisfy the given conditions.

print(solution())