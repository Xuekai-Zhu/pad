def solution():
    
    flour = 2
    white_sugar = 1
    brown_sugar = 0.25
    oil = 0.5
    scoop = 0.25
    flour_scoops = flour / scoop
    white_sugar_scoops = white_sugar / scoop
    brown_sugar_scoops = brown_sugar / scoop
    oil_scoops = oil / scoop
    total_scoops = int(flour_scoops + white_sugar_scoops + brown_sugar_scoops + oil_scoops)
    result = total_scoops
    return result

print(solution())