def solution():
    
    flour_cups = 3
    sugar_cups = 2
    scoop_size = 1/3
    total_flour_scoops = flour_cups / scoop_size
    total_sugar_scoops = sugar_cups / scoop_size
    total_scoops = total_flour_scoops + total_sugar_scoops
    result = total_scoops
    return result

print(solution())