def solution():
    """Louise is organizing her pencils, and decides she wants her boxes arranged by color. Each box holds 20 pencils each. She has 20 red pencils, twice as many blue pencils, 40 yellow pencils, and has as many green pencils as she has red and blue pencils combined. How many boxes does Louise need?"""
    # Calculate the number of blue pencils
    blue_pencils = 20 * 2

    # Calculate the total number of red and blue pencils
    red_blue_pencils = 20 + blue_pencils 

    # Calculate the number of green pencils
    green_pencils = red_blue_pencils

    # Calculate the total number of pencils
    total_pencils = 20 + blue_pencils + 40 + green_pencils

    # Calculate the number of boxes needed
    boxes = total_pencils // 20

    # return the result
    result = boxes
    return result

print(solution())