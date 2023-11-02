def solution():
    """Louise is organizing her pencils, and decides she wants her boxes arranged by color. Each box holds 20 pencils each. She has 20 red pencils, twice as many blue pencils, 40 yellow pencils, and has as many green pencils as she has red and blue pencils combined. How many boxes does Louise need?"""
    red_pencils = 20
    blue_pencils = red_pencils * 2
    yellow_pencils = 40
    green_pencils = red_pencils + blue_pencils
    total_pencils = red_pencils + blue_pencils + yellow_pencils + green_pencils
    boxes_needed = total_pencils // 20
    result = boxes_needed
    return result

print(solution())