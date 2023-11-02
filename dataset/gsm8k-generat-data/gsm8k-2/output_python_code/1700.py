def solution():
    """Sandra has a box of apples that weighs 120 pounds. She's going to use half the weight in apples to make applesauce.
    The rest will be used to make apple pies. She needs 4 pounds of apples per pie. How many pies will she be able to make?"""
    total_weight = 120
    apple_sauce_weight = total_weight / 2
    pie_weight = total_weight - apple_sauce_weight
    pies = pie_weight / 4
    result = pies
    return result

print(solution())