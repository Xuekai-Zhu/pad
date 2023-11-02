def solution():
    """Mark is looking to buy a total of 12 pieces of fruit at the store. He has already chosen 3 apples. He has also selected a bunch of bananas containing 4 bananas. How many oranges does he need to pick out to have 12 total pieces of fruit?"""
    total_fruit = 12
    apples = 3
    bananas = 4
    oranges = total_fruit - apples - bananas
    result = oranges
    return result

print(solution())