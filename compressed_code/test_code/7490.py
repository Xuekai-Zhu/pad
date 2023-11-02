def solution():
    
    flour = 2
    white_sugar = 1
    brown_sugar = 0.25
    oil = 0.5
    measuring_scoop = 0.25
    flour_scoops = flour / measuring_scoop
    white_sugar_scoops = white_sugar / measuring_scoop
    brown_sugar_scoops = brown_sugar / measuring_scoop
    oil_scoops = oil/ measuring_scoop
    total_scoops = flour_scoops + white_sugar_scoops + brown_sugar_scoops + oil_scoops
    result = total_scoops
    return result

print(solution())