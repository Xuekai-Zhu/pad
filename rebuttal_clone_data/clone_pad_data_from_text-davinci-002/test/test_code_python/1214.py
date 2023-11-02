def solution():
    flour = 2
    white_sugar = 1
    brown_sugar = 1/4
    oil = 1/2
    measuring_scoop = 1/4
    total_cups = flour + white_sugar + brown_sugar + oil
    result = total_cups / measuring_scoop
    return result

print(solution())