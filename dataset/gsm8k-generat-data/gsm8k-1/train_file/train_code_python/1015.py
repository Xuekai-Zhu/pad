def solution():
    """There are 78 pieces of fruit in a crate. One-third of the box contains kiwi. The rest are strawberries. How many strawberries are there?"""
    total_fruit = 78
    kiwis = total_fruit / 3
    strawberries = total_fruit - kiwis
    result = strawberries
    return result

print(solution())