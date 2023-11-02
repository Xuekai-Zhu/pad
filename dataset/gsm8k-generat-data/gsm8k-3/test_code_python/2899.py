def solution():
    """Mark went to a store where he spent one-half of his money, and then spent $14 more. He then went to another store where he spent one-third of his starting money, and then spent $16 more. If he then had no money left, how much did he have when he entered the first store?"""
    # Let x be Mark's starting money
    # Mark spent half of his money at the first store, so he has x/2 left
    # Mark then spent $14 more, so he has x/2 - 14 left
    # Mark spent one-third of his starting money at the second store, so he has 2/3*x left
    # Mark then spent $16 more, so he has 2/3*x - 16 left
    # Since Mark has no money left at the end, we have:
    # x/2 - 14 + 2/3*x - 16 = 0

    # Solving for x:
    x = 132

    # Display Mark's starting money
    result = x
    return result

print(solution())