def solution():
    """Gracie was 7 inches shorter than Grayson. Grayson was 2 inches taller than Griffin. Griffin is 61 inches tall. How many inches tall is Gracie?"""
    # Define the height of Griffin
    griffin_height = 61

    # Calculate the height of Grayson
    grayson_height = griffin_height + 2

    # Calculate the height of Gracie
    gracie_height = grayson_height - 7

    # Display the height of Gracie
    result = gracie_height
    return result

print(solution())