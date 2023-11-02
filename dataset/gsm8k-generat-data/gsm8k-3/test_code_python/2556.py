def solution():
    """One white rhino weighs 5100 pounds and one black rhino weighs 1 ton. How many pounds would 7 white rhinos and 8 black rhinos weigh in total?"""
    # Convert weight of one black rhino from tons to pounds
    BLACK_RHINO_WEIGHT = 2000

    # Calculate the total weight of all white rhinos
    white_rhino_weight = 7 * 5100

    # Calculate the total weight of all black rhinos
    black_rhino_weight = 8 * BLACK_RHINO_WEIGHT

    # Calculate the total weight of all rhinos
    total_weight = white_rhino_weight + black_rhino_weight

    # Display the total weight of all rhinos
    result = total_weight
    return result

print(solution())