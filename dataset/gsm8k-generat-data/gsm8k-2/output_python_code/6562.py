def solution():
    """Jack has four plates with a flower pattern and 8 plates with a checked pattern. He buys new twice as many polka dotted plates as the number of checked plates he currently has, then smashes one of the flowered plates. How many plates does he have left?"""
    flower_plates = 4
    checked_plates = 8
    polka_dotted_plates = 2 * checked_plates
    total_plates = flower_plates + checked_plates + polka_dotted_plates - 1
    result = total_plates
    return result

print(solution())