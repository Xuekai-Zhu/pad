def solution():
    """James buys 3 CDs. Two of them are 1.5 hours each. The last one is twice that long. What is the combined length of the CDs?"""
    # Define the length of the first two CDs
    cd1_length = 1.5
    cd2_length = 1.5

    # Define the length of the third CD
    cd3_length = cd2_length * 2

    # Calculate the combined length of the three CDs
    total_length = cd1_length + cd2_length + cd3_length

    result = total_length
    return result

print(solution())