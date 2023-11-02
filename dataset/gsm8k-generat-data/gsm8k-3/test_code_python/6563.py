def solution():
    """Jack has four plates with a flower pattern and 8 plates with a checked pattern. He buys new twice as many polka dotted plates as the number of checked plates he currently has, then smashes one of the flowered plates. How many plates does he have left?"""
    # Define the initial number of flowered and checked plates
    flowered_plates = 4
    checked_plates = 8

    # Calculate the number of polka dotted plates Jack buys
    polka_dotted_plates = 2 * checked_plates

    # Subtract one smashed flowered plate from the total number of plates
    total_plates = flowered_plates + checked_plates + polka_dotted_plates - 1

    # Display the total number of plates Jack has left
    result = total_plates
    return result

print(solution())