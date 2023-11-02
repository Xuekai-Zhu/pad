def solution():
    """Mitch is baking a cake and needs 3 cups of flour and two cups of sugar. He doesn't have a one cup scoop, only a 1/3 cup scoop. How many total scoops will he need?"""
    flour_cups = 3
    sugar_cups = 2
    scoop_size = 1/3
    total_flour_scoops = flour_cups / scoop_size
    total_sugar_scoops = sugar_cups / scoop_size
    total_scoops = total_flour_scoops + total_sugar_scoops
    result = total_scoops
    return result

print(solution())