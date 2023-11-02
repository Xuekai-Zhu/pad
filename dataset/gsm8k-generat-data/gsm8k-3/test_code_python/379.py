def solution():
    """James buys 3 CDs. Two of them are 1.5 hours each. The last one is twice that long. What is the combined length of the CDs?"""
    # Define the length of the two 1.5 hour CDs
    CD1_LENGTH = 1.5
    CD2_LENGTH = 1.5

    # Define the length of the third CD
    CD3_LENGTH = CD1_LENGTH * 2

    # Calculate the combined length of all three CDs
    total_length = CD1_LENGTH + CD2_LENGTH + CD3_LENGTH

    # Display the combined length of the CDs
    result = total_length
    return result

print(solution())