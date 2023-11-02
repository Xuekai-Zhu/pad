def solution():
    """Jack has four plates with a flower pattern and 8 plates with a checked pattern. He buys new twice as many polka dotted plates as the number of checked plates he currently has, then smashes one of the flowered plates. How many plates does he have left?"""
    # Define the initial number of plates
    flower_plates = 4
    checked_plates = 8

    # Calculate the number of polka dotted plates bought
    polka_plates = 2 * checked_plates

    # Calculate the total number of plates
    total_plates = flower_plates + checked_plates + polka_plates

    # Subtract one of the flowered plates that was smashed
    total_plates -= 1

    # Return the result
    result = total_plates
    return result

print(solution())