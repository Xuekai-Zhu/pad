def solution():
    """Gracie was 7 inches shorter than Grayson. Grayson was 2 inches taller than Griffin. Griffin is 61 inches tall. How many inches tall is Gracie?"""
    # Define Griffin's height
    griffin_height = 61

    # Calculate Grayson's height
    grayson_height = griffin_height + 2

    # Calculate Gracie's height
    gracie_height = grayson_height - 7

    # return the result
    result = gracie_height
    return result

print(solution())