def solution():
    """Louise is organizing her pencils, and decides she wants her boxes arranged by color. Each box holds 20 pencils each. She has 20 red pencils, twice as many blue pencils, 40 yellow pencils, and has as many green pencils as she has red and blue pencils combined. How many boxes does Louise need?"""
    # Define the number of pencils per box
    PENCILS_PER_BOX = 20

    # Calculate the number of blue pencils Louise has
    blue_pencils = 20 * 2

    # Calculate the number of green pencils Louise has
    green_pencils = 20 + blue_pencils

    # Calculate the total number of pencils
    total_pencils = 20 + blue_pencils + 40 + green_pencils

    # Calculate the number of boxes Louise needs
    boxes_needed = total_pencils // PENCILS_PER_BOX

    # Display the number of boxes needed
    result = boxes_needed
    return result

print(solution())