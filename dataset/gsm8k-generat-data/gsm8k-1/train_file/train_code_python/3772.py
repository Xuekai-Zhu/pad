def solution():
    """A packet of candy sweets has 30 cherry-flavored sweets, 40 strawberry-flavored sweets, and 50 pineapple-flavored sweets. Aaron eats half of each of the flavored sweets and gives 5 cherry-flavored sweets to his friend. How many sweets are still in the packet of candy?"""
    cherry_sweets = 30
    strawberry_sweets = 40
    pineapple_sweets = 50
    eaten_sweets = (cherry_sweets + strawberry_sweets + pineapple_sweets) / 2
    cherry_sweets -= 0.5 * cherry_sweets
    strawberry_sweets -= 0.5 * strawberry_sweets
    pineapple_sweets -= 0.5 * pineapple_sweets
    cherry_sweets -= 5
    total_sweets = cherry_sweets + strawberry_sweets + pineapple_sweets
    remaining_sweets = total_sweets - eaten_sweets
    result = remaining_sweets
    return result

print(solution())