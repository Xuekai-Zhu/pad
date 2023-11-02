def solution():
    """Mitch is baking a cake and needs 3 cups of flour and two cups of sugar. He doesn't have a one cup scoop, only a 1/3 cup scoop. How many total scoops will he need?"""
    flour_scoops = 9  # 3 cups * 3 scoops per cup (1/3 cup scoop)
    sugar_scoops = 6  # 2 cups * 3 scoops per cup (1/3 cup scoop)
    total_scoops = flour_scoops + sugar_scoops
    result = total_scoops
    return result

print(solution())