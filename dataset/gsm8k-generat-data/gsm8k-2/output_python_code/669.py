def solution():
    """Gracie was 7 inches shorter than Grayson. Grayson was 2 inches taller than Griffin. Griffin is 61 inches tall. How many inches tall is Gracie?"""
    griffin_height = 61
    grayson_height = griffin_height + 2
    gracie_height = grayson_height - 7
    result = gracie_height
    return result

print(solution())